from unittest import TestCase

from areas import Test


class CountRangeTest(TestCase):
    def test_riscv(self):
        submission_path = "./tests/resources/count_range/submission.zip"
        subroutine_path = "./tests/resources/count_range/subroutines.yaml"
        tests_path = "./tests/resources/count_range/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result['subroutines'][0]['score']

        self.assertAlmostEqual(score, 0)

    def test_arm(self):
        submission_path = "./tests/resources/count_range/submission.zip"
        subroutine_path = "./tests/resources/count_range/subroutines_arm.yaml"
        tests_path = "./tests/resources/count_range/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        # assert compile error
        self.assertFalse(result["subroutines"][0]["compiled"])

    def test_riscv_godbolt(self):
        submission_path = "./tests/resources/count_range/goldbolt_disassembler_riscv/submission.zip"
        subroutine_path = "./tests/resources/count_range/subroutines.yaml"
        tests_path = "./tests/resources/count_range/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result['subroutines'][0]['score']

        self.assertAlmostEqual(score, 1.0)

    def test_arm_godbolt(self):
        submission_path = "./tests/resources/count_range/goldbolt_disassembler_arm64/submission.zip"
        subroutine_path = "./tests/resources/count_range/subroutines_arm.yaml"
        tests_path = "./tests/resources/count_range/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result['subroutines'][0]['score']

        self.assertAlmostEqual(score, 1.0)
