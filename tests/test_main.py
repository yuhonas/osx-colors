import unittest
from unittest import mock
from src.__main__ import get_args, parse_args


@mock.patch("src.__main__.run")
class TestMain(unittest.TestCase):
    def test_set_colors_to_green(self, run_mock):
        parser = get_args()

        parse_args(parser, ["set", "green", "--quiet"])

        self.assertIn(
            mock.call(["defaults", "write", "-g", "AppleAccentColor", "-int", "3"], check=True),
            run_mock.call_args_list,
        )

        self.assertIn(
            mock.call(
                [
                    "defaults",
                    "write",
                    "-g",
                    "AppleHighlightColor",
                    "-string",
                    "0.752941 0.964706 0.678431 Green",
                ],
                check=True,
            ),
            run_mock.call_args_list,
        )

        self.assertIn(mock.call(["killall", "Finder"], check=True), run_mock.call_args_list)

        self.assertIn(mock.call(["killall", "Spotlight"], check=True), run_mock.call_args_list)

        self.assertIn(
            mock.call(
                ["osascript", "-e", 'tell application "System Preferences" to quit'],
                check=True,
            ),
            run_mock.call_args_list,
        )
