from unittest import TestCase

from areas import Test


class TestRun(TestCase):
    def test_run(self):
        submission_path = "./tests/resources/warning_error/submission.zip"
        subroutine_path = "./tests/resources/count_range/subroutines_arm.yaml"
        tests_path = "./tests/resources/count_range/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        subroutine = result["subroutines"][0]

        self.assertEqual(len(subroutine["compilation_errors"]["warnings"]), 1)
        self.assertEqual(len(subroutine["compilation_errors"]["errors"]), 2)

    def test_run_riscv(self):
        submission_path = "./tests/resources/warning_error/submission.zip"
        subroutine_path = "./tests/resources/count_range/subroutines.yaml"
        tests_path = "./tests/resources/count_range/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        subroutine = result["subroutines"][0]

        self.assertEqual(len(subroutine["compilation_errors"]["warnings"]), 1)
        self.assertEqual(len(subroutine["compilation_errors"]["errors"]), 17)
