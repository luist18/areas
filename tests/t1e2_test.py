from unittest import TestCase

from areas import Test


class T1E2Test(TestCase):
    def test_run(self):
        submission_path = "./tests/resources/t1e2/submission.zip"
        subroutine_path = "./tests/resources/t1e2/subroutines.yaml"
        tests_path = "./tests/resources/t1e2/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result["subroutines"][0]["score"]

        self.assertAlmostEqual(score, 1.0)
