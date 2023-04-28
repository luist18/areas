import json
from datetime import datetime
from re import IGNORECASE, match

from yaml import YAMLError, safe_load

import areas.util.subroutine_integrity as subroutine_integrity
from areas.exception import ToolFileError
from areas.subroutines import ArraySubroutine as Array
from areas.subroutines import MixedSubroutine as Mixed
from areas.subroutines import NumericSubroutine as Numeric
from areas.subroutines import VoidSubroutine as Void
from areas.tester import Tester


class Test:
    def __init__(
        self,
        submission_file,
        subroutine_file=None,
        tests_file=None,
        subroutines=None,
        test_suite=None,
        timeout=1,
        float_threshold=1e-6,
        save_to_file=False,
    ):
        self.submission_file = submission_file
        self.subroutine_file = subroutine_file
        self.tests_file = tests_file

        # files always override manual definitions
        self.subroutines = subroutines
        self.test_suite = test_suite

        self.timeout = timeout
        self.float_threshold = float_threshold
        self.save_to_file = save_to_file

        self.__read_files()
        self.__parse_inputs()
        self.__build_test_cases()

    def __parse_inputs(self):
        for key in self.subroutines:
            if key not in self.test_suite:
                raise ToolFileError(f"Subroutine {key} is not in the test suite")
            else:
                subroutine = self.subroutines[key]
                test_suite = self.test_suite[key]

                subroutine_integrity.parse_subroutine(subroutine, test_suite)

    def __load_file(self, file):
        ext = file.split(".")[-1]

        if ext == "json":
            return json.load(open(file))
        elif ext == "yaml" or ext == "yml":
            return safe_load(open(file))
        else:
            raise ToolFileError("File extension not supported: {}".format(ext))

    def __read_files(self):
        try:
            if self.subroutine_file is not None:
                self.subroutines = self.__load_file(self.subroutine_file)

            if self.tests_file is not None:
                self.test_suite = self.__load_file(self.tests_file)
        except IOError as err:
            raise ToolFileError(
                "Could not open: {}, please specify a valid file".format(str(err))
            )
        except YAMLError as err:
            raise ToolFileError(
                "Error parsing YAML files: ({}), please correct syntax".format(str(err))
            )

    def __build_subroutine(self, name, definition):
        map_to_truth_value = [
            "array" in ret or ret == "string" for ret in definition["return"]
        ]

        architecture = (
            definition["architecture"] if "architecture" in definition else "arm"
        )

        if not len(map_to_truth_value):  # No returns - void subroutine
            return Void(name, definition["params"], architecture)
        elif all(map_to_truth_value):  # Only arrays and/or strings as return values
            return Array(name, definition["params"], definition["return"], architecture)
        elif not any(map_to_truth_value):  # Numeric output
            return Numeric(
                name, definition["params"], definition["return"][0], architecture
            )
        else:  # Mixed return
            return Mixed(
                name,
                definition["params"],
                definition["return"][0],
                definition["return"][1:],
                architecture,
            )

    def __build_test_cases(self):
        self.subroutine_objects = {
            name: self.__build_subroutine(name, definition)
            for name, definition in self.subroutines.items()
        }

    def run(self):
        folder_prefix = str(datetime.now().microsecond)

        grading_folder = f"tmp_{folder_prefix}_grading"
        feedback_folder = f"tmp_{folder_prefix}_feedback"

        try:
            tester = Tester(
                self.subroutine_objects,
                self.test_suite,
                grading_folder=grading_folder,
                feedback_folder=feedback_folder,
                float_threshold=self.float_threshold,
                timeout=self.timeout,
                save_to_file=self.save_to_file,
            )

            submission = tester.grade_submission(self.submission_file)

            filename = match(
                r"(?:.+\/)*(.*)?.*\.zip", self.submission_file, flags=IGNORECASE
            ).group(1)

            return {
                "submission_name": filename,
                "subroutines": submission,
            }
        except Exception as err:
            raise err
        finally:
            import shutil

            shutil.rmtree(grading_folder, ignore_errors=True)
            shutil.rmtree(feedback_folder, ignore_errors=True)
