from unittest import TestCase

from areas import Test
from areas.exception import ToolFileError

RESOURCES_PATH = "./tests/resources/definition_errors/"


class ErrorsTest(TestCase):

    def test_invalid_file_extension(self):
        submission_path = RESOURCES_PATH + "submission.zip"
        subroutine_path = RESOURCES_PATH + "invalid_file_ext/subroutines.txt"
        tests_path = RESOURCES_PATH + "invalid_params/tests.yaml"

        with self.assertRaises(ToolFileError) as context:
            test = Test(submission_path, subroutine_path, tests_path)
            test.run()

        self.assertEqual(str(context.exception),
                         "File extension not supported: txt")

    def test_subroutine_without_tests(self):
        submission_path = RESOURCES_PATH + "submission.zip"
        subroutine_path = RESOURCES_PATH + "without_tests/subroutines.yaml"
        tests_path = RESOURCES_PATH + "without_tests/tests.yaml"

        with self.assertRaises(ToolFileError) as context:
            test = Test(submission_path, subroutine_path, tests_path)
            test.run()

        self.assertEqual(str(context.exception),
                         "Subroutine func is not in the test suite")

    def test_invalid_param(self):
        submission_path = RESOURCES_PATH + "submission.zip"
        subroutine_path = RESOURCES_PATH + "invalid_params/subroutines.yaml"
        tests_path = RESOURCES_PATH + "invalid_params/tests.yaml"

        with self.assertRaises(ToolFileError) as context:
            test = Test(submission_path, subroutine_path, tests_path)
            test.run()

        self.assertEqual(str(context.exception),
                         "Parameter type inta not supported")

    def test_invalid_return(self):
        submission_path = RESOURCES_PATH + "submission.zip"
        subroutine_path = RESOURCES_PATH + "invalid_return/subroutines.yaml"
        tests_path = RESOURCES_PATH + "invalid_return/tests.yaml"

        with self.assertRaises(ToolFileError) as context:
            test = Test(submission_path, subroutine_path, tests_path)
            test.run()

        self.assertEqual(str(context.exception),
                         "Return type intx not supported")

    def test_no_params(self):
        submission_path = RESOURCES_PATH + "submission.zip"
        subroutine_path = RESOURCES_PATH + "no_params/subroutines.yaml"
        tests_path = RESOURCES_PATH + "no_params/tests.yaml"

        with self.assertRaises(ToolFileError) as context:
            test = Test(submission_path, subroutine_path, tests_path)
            test.run()

        self.assertEqual(str(context.exception),
                         "No parameters in subroutine definition")

    def test_invalid_architecture(self):
        submission_path = RESOURCES_PATH + "submission.zip"
        subroutine_path = RESOURCES_PATH + "invalid_architecture/subroutines.yaml"
        tests_path = RESOURCES_PATH + "invalid_architecture/tests.yaml"

        with self.assertRaises(ToolFileError) as context:
            test = Test(submission_path, subroutine_path, tests_path)
            test.run()

        self.assertEqual(str(context.exception),
                         "Architecture arms is not supported")

    def test_no_inputs(self):
        pass

    def test_no_outputs(self):
        pass

    # test errors

    def test_input_length_mismatch(self):
        pass

    def test_output_length_mismatch(self):
        pass

    def test_input_type_mismatch(self):
        pass

    def test_output_type_mismatch(self):
        pass
