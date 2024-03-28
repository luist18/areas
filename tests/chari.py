from unittest import TestCase

from areas import Test


class Chari(TestCase):
    def test_run(self):
        submission_path = "./tests/resources/chari/submission.zip"
        subroutine_path = "./tests/resources/chari/subroutines.yaml"
        tests_path = "./tests/resources/chari/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        score = result["subroutines"][0]["score"]

        self.assertAlmostEqual(score, 1.0)
