import runner_2
import unittest


class TournamentTest(unittest.TestCase):

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

    def test1(self):
        t1 = runner_2.Tournament(90, self.run1, self.run3)
        TournamentTest.all_results = t1.start()
        self.assertTrue(TournamentTest.all_results[2] == self.run3)

    def test2(self):
        t2 = runner_2.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results = t2.start()
        self.assertTrue(TournamentTest.all_results[2] == self.run3)

    def test3(self):
        t3 = runner_2.Tournament(90, self.run2, self.run1, self.run3)
        TournamentTest.all_results = t3.start()
        self.assertTrue(TournamentTest.all_results[3] == self.run3)


if __name__ == "__main__":
    unittest.main
