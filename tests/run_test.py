from unittest import TestCase

from areas import Test


class TestRun(TestCase):
    def test_run(self):
        submission_path = "./tests/resources/submission.zip"
        subroutine_path = "./tests/resources/subroutines.yaml"
        tests_path = "./tests/resources/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result['subroutines'][0]['score']

        self.assertAlmostEqual(score, 1.0)

    def test_riscv_json(self):
        pass

    def test_riscv_yaml(self):
        pass

    def test_riscv_manual(self):
        subroutines = {
            "func": {
                "architecture": "riscv",
                "params": ["int", "int", "int"],
                "return": ["int"]
            }
        }

        tests = {
            "func": [
                {
                    "inputs": [1, 2, 3],
                    "outputs": [5],
                    "weight": 0.5
                },
                {
                    "inputs": [10, 20, 0],
                    "outputs": [200],
                    "weight": 0.5
                }
            ]
        }

        submission_path = "./tests/resources/riscv/submission.zip"

        test = Test(submission_path, subroutines=subroutines, test_suite=tests)

        result = test.run()

        score = result['subroutines'][0]['score']

        self.assertAlmostEqual(score, 1.0)
