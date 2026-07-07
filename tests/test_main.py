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

    @mock.patch("src.__main__.logging.getLogger")
    def test_get_color_purple(self, mock_get_logger, run_mock):
        parser = get_args()
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        def run_side_effect(cmd, *args, **kwargs):
            mock_res = mock.Mock()
            if cmd == ["defaults", "read", "-g", "AppleAccentColor"]:
                mock_res.stdout = "5\n"
            elif cmd == ["defaults", "read", "-g", "AppleHighlightColor"]:
                mock_res.stdout = "0.968627 0.831373 1.000000 Purple\n"
            else:
                raise Exception("Unexpected command")
            return mock_res

        run_mock.side_effect = run_side_effect

        parse_args(parser, ["get"])
        mock_logger.info.assert_called_with("purple")

    @mock.patch("src.__main__.logging.getLogger")
    def test_get_color_unknown(self, mock_get_logger, run_mock):
        from subprocess import CalledProcessError

        parser = get_args()
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        # Let the commands raise subprocess error / return empty values to simulate unknown/unset
        run_mock.side_effect = CalledProcessError(1, "defaults")

        parse_args(parser, ["get"])
        mock_logger.error.assert_called_with("Unknown Color")

    def test_set_color_requires_argument(self, run_mock):
        parser = get_args()
        with self.assertRaises(SystemExit):
            parse_args(parser, ["set"])
