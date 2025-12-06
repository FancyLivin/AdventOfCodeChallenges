import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('test_input_one.txt')
    
    def test_store_races(self):
        races = {
            'race1': {'Time': 7, 'Distance': 9},
            'race2': {'Time': 15, 'Distance': 40},
            'race3': {'Time': 30, 'Distance': 200}
        }
        self.assertEqual(self.part_one.races, races)

    def test_get_total_record_beaters(self):
        total_records = self.part_one.get_total_record_beaters()

        self.assertEqual(total_records, 288)

    def test_get_current_race_record_beaters(self):
        race_one_records = self.part_one.get_current_race_record('race1')
        race_two_records = self.part_one.get_current_race_record('race2')
        race_three_records = self.part_one.get_current_race_record('race3')

        self.assertEqual(race_one_records, 4)
        self.assertEqual(race_two_records, 8)
        self.assertEqual(race_three_records, 9)

    def test_is_record_breaking(self):
        record_breaker = self.part_one.is_record_breaking('race1', 2)
        not_record_breaking = self.part_one.is_record_breaking('race1', 0)

        self.assertTrue(record_breaker)
        self.assertFalse(not_record_breaking)


class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.part_two = m.PartTwo('test_input_one.txt')

    def test_store_race(self):
        race = {'race1': {'Time': 71530, 'Distance': 940200}}
        self.assertEqual(self.part_two.race, race)

    def test_get_total_record_beaters(self):
        record_beaters = self.part_two.get_total_record_beaters()
        self.assertEqual(record_beaters, 71503)
