from unittest import TestCase

from areas import Test


class TransformTest(TestCase):
    def test_transform(self):
        pass
        submission_path = "./tests/resources/transform/submission.zip"
        subroutine_path = "./tests/resources/transform/subroutines.yaml"
        tests_path = "./tests/resources/transform/tests.yaml"

        test = Test(submission_path, subroutine_path, tests_path)

        result = test.run()

        print("ERROR: ", result["subroutines"][0]["compile_output"])

        score = result['subroutines'][0]['score']

        self.assertAlmostEqual(score, 1)
