import unittest
import tests_12_3

test_rt = unittest.TestSuite()
test_rt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_rt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_rt)