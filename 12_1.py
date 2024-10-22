import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run1 = runner.Runner('Егор')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run2 = runner.Runner('Ваня')
        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_chalange(self):
        run3 = runner.Runner('Олег')
        run4 = runner.Runner('Оля')
        for i in range(10):
            run3.walk()
            run4.run()
        self.assertNotEqual(run3.distance, run4.distance)


if __name__ == "__main__":
    unittest.main()
