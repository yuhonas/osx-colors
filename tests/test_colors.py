""" Some basic sanity tests """
import unittest
from src.color_utils import closest_colors_to

class TestGenColors(unittest.TestCase):

    def test_apple_blue(self):
        self.assertEqual(
          closest_colors_to('#007aff'), (4, "0.698039 0.843137 1.000000 Blue")
        )

    def test_apple_purple(self):
        self.assertEqual(
          closest_colors_to('#a550a7'), (5, "0.968627 0.831373 1.000000 Purple")
        )

    def test_apple_pink(self):
        self.assertEqual(
          closest_colors_to('#f74f9e'), (6, "1.000000 0.749020 0.823529 Pink" )
        )

    def test_apple_red(self):
        self.assertEqual(
          closest_colors_to('#ff5257'), (0, "1.000000 0.733333 0.721569 Red")
        )

    def test_apple_orange(self):
        self.assertEqual(
          closest_colors_to('#f7821b'), (1, "1.000000 0.874510 0.701961 Orange")
        )

    def test_apple_yellow(self):
        self.assertEqual(
          closest_colors_to('#ffc600'), (2, "1.000000 0.937255 0.690196 Yellow" )
        )

    def test_apple_green(self):
        self.assertEqual(
          closest_colors_to('#62ba46'), (3, "0.752941 0.964706 0.678431 Green")
        )

    def test_apple_graphite(self):
        self.assertEqual(
          closest_colors_to('#8c8c8c'), ("-1",  "0.847059 0.847059 0.862745 Graphite")
        )
