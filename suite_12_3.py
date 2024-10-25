import unittest
import tests_12_3

testsST = unittest.TestSuite()
testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
rec = unittest.TextTestRunner(verbosity=2)
rec.run(testsST)
