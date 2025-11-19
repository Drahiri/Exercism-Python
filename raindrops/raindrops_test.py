import unittest

from raindrops import convert


class RaindropsTest(unittest.TestCase):
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1")

    def test_the_sound_of_3_is_pling(self):
        self.assertEqual(convert(3), "Pling")

    def test_the_sound_of_5_is_plang(self):
        self.assertEqual(convert(5), "Plang")

    def test_the_sound_of_7_is_plong(self):
        self.assertEqual(convert(7), "Plong")

    def test_the_sound_of_6_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(6), "Pling")

    def test_2_to_the_power_of_3_does_not_make_a_raindrop_sound_as_3_is_the_exponent_not_the_base(
        self,
    ):
        self.assertEqual(convert(8), "8")

    def test_the_sound_of_9_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(9), "Pling")

    def test_the_sound_of_10_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(10), "Plang")

    def test_the_sound_of_14_is_plong_as_it_has_a_factor_of_7(self):
        self.assertEqual(convert(14), "Plong")

    def test_the_sound_of_15_is_pling_plang_as_it_has_factors_3_and_5(self):
        self.assertEqual(convert(15), "PlingPlang")

    def test_the_sound_of_21_is_pling_plong_as_it_has_factors_3_and_7(self):
        self.assertEqual(convert(21), "PlingPlong")

    def test_the_sound_of_25_is_plang_as_it_has_a_factor_of_5(self):
        self.assertEqual(convert(25), "Plang")

    def test_the_sound_of_27_is_pling_as_it_has_a_factor_of_3(self):
        self.assertEqual(convert(27), "Pling")

    def test_the_sound_of_35_is_plang_plong_as_it_has_factors_5_and_7(self):
        self.assertEqual(convert(35), "PlangPlong")

    def test_the_sound_of_49_is_plong_as_it_has_factor_of_7(self):
        self.assertEqual(convert(49), "Plong")

    def test_the_sound_of_52_is_52(self):
        self.assertEqual(convert(52), "52")

    def test_the_sound_of_105_is_pling_plang_plong_as_it_has_factors_3_5_and_7(self):
        self.assertEqual(convert(105), "PlingPlangPlong")

    def test_the_sound_of_3125_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(3125), "Plang")
