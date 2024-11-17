import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_ = runner_and_tournament.Runner('Ivan')
        for i in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_ran(self):
        runner_ = runner_and_tournament.Runner('Ivan')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = runner_and_tournament.Runner('Ivan1')
        runner_2 = runner_and_tournament.Runner('Ivan2')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)




class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
         self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
         self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
         self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            temp_dict = {}
            for j in cls.all_results[i]:
                temp_dict[j] = str(cls.all_results[i][j])
            print(temp_dict)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        tournament1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = tournament1.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1].keys())] == 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        tournament2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = tournament2.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2].keys())] == 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        tournament3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = tournament3.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3].keys())] == 'Ник')


if __name__ == "__main__":
    unittest.main()

