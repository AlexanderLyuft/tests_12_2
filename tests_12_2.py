        # Домашнее задание по теме "Методы Юнит-тестирования"


import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        for participant in self.participants:
            time_to_finish = self.full_distance / (participant.speed * 2)
            finishers[participant] = time_to_finish

        sorted_finishers = sorted(finishers.items(), key=lambda x: x[1])
        results = {}
        for place, (runner, _) in enumerate(sorted_finishers, start=1):
            results[place] = runner

        return results

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {1: results[1].name, 2: results[2].name}
        print(self.all_results[max(results.keys())])
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {1: results[1].name, 2: results[2].name}
        print(self.all_results[max(results.keys())])
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_all(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {1: results[1].name, 2: results[2].name, 3: results[3].name}
        print(self.all_results[max(results.keys())])
        self.assertTrue(results[max(results.keys())].name == "Ник")

if __name__ == '__main__':
    unittest.main()





