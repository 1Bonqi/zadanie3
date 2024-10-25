import runner_2
import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "ok")
    def test_walk(self):
        run1 = runner.Runner('Егор')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    @unittest.skipIf(is_frozen, 'ok')
    def test_run(self):
        run2 = runner.Runner('Ваня')
        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    @unittest.skipIf(is_frozen, 'ok' )
    def test_chalange(self):
        run3 = runner.Runner('Олег')
        run4 = runner.Runner('Оля')
        for i in range(10):
            run3.walk()
            run4.run()
        self.assertNotEqual(run3.distance, run4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = runner_2.Runner('Усейн', 10)
        self.run2 = runner_2.Runner('Андрей', 9)
        self.run3 = runner_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        t1 = runner_2.Tournament(90, self.run1, self.run3)
        TournamentTest.all_results = t1.start()
        self.assertTrue(TournamentTest.all_results[2] == self.run3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        t2 = runner_2.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results = t2.start()
        self.assertTrue(TournamentTest.all_results[2] == self.run3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        t3 = runner_2.Tournament(90, self.run2, self.run1, self.run3)
        TournamentTest.all_results = t3.start()
        self.assertTrue(TournamentTest.all_results[3] == self.run3)


if __name__ == "__main__":
    unittest.main
