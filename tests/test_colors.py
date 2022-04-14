""" Some basic sanity tests """
import unittest
import src.colors as colors

class TestGenColors(unittest.TestCase):

    def test_apple_blue(self):
        self.assertEqual( colors.closest_colors_to('#007aff', 'apple'), 4)

    def test_apple_purple(self):
        self.assertEqual( colors.closest_colors_to('#a550a7', 'apple'), 5)

    def test_apple_pink(self):
        self.assertEqual( colors.closest_colors_to('#f74f9e', 'apple'), 6)

    def test_apple_red(self):
        self.assertEqual( colors.closest_colors_to('#ff5257', 'apple'), 0)

    def test_apple_orange(self):
        self.assertEqual( colors.closest_colors_to('#f7821b', 'apple'), 1)

    def test_apple_yellow(self):
        self.assertEqual( colors.closest_colors_to('#ffc600', 'apple'), 2)

    def test_apple_green(self):
        self.assertEqual( colors.closest_colors_to('#62ba46', 'apple'), 3)

    def test_apple_graphite(self):
        self.assertEqual( colors.closest_colors_to('#8c8c8c', 'apple'), "-1")
