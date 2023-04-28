from unittest import TestCase

from areas import Test


class RISCVExtern(TestCase):
    def test_extern(self):
        submission_path = "./tests/resources/riscv_extern/submission.zip"
        subroutine_path = "./tests/resources/riscv_extern/subroutines.yaml"
        tests_path = "./tests/resources/riscv_extern/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result["subroutines"][0]["score"]

        self.assertAlmostEqual(score, 1)

    def test_extern_jal(self):
        submission_path = "./tests/resources/riscv_extern/jal/submission.zip"
        subroutine_path = "./tests/resources/riscv_extern/subroutines.yaml"
        tests_path = "./tests/resources/riscv_extern/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result["subroutines"][0]["score"]

        self.assertAlmostEqual(score, 1)
