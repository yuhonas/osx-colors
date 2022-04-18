import argparse
from subprocess import run
import sys
import logging
from textwrap import dedent

from .color_utils import closest_colors_to, APPLE_COLORS
from . import settings

logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)


def get_args():
    """Get the script arguments"""
    parser = argparse.ArgumentParser(
        description="Sane command line color customization for osx",
        prog=settings.get_app_name(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent(
            f"""
        Examples:
        # To set osx to use apples green
        $ {settings.get_app_name()} set green

        # To set the color based on closest matching apple color to a supplied one
        $ {settings.get_app_name()} set ff001d
      """
        ),
    )

    # NOTE: This is more of a placeholder at current to support potentially adding a
    # read action or others and it also just looks plain weird without a verb after the command
    parser.add_argument(
        "action", choices=["set"], help="action to perform, only 'set' is supported currently"
    )

    parser.add_argument("color", help="color to set (" + "|".join(APPLE_COLORS) + ") or a hex color")

    parser.add_argument("-q", "--quiet", help="quiet mode, don't output anything", action="store_true")

    parser.add_argument(
        "-s",
        "--skip-restart",
        action="store_true",
        help="skip restarting Finder, Spotlight and System Preferences",
    )

    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {settings.get_version()}")

    return parser


def parse_args(parser, args):
    """Parse script arguments"""
    parsed_args = parser.parse_args(args=args)

    logger = logging.getLogger()

    if parsed_args.quiet:
        logger.disabled = True

    if parsed_args.color in APPLE_COLORS:
        closest_color_name = parsed_args.color
        closest_color = APPLE_COLORS[parsed_args.color]
    else:
        closest_color_name, closest_color = closest_colors_to(parsed_args.color)

        logger.info(
            "Searching for the closest Apple color to '%s' found '%s'",
            parsed_args.color,
            closest_color_name,
        )

    logger.info("Setting the 'Accent Color' to '%s'", closest_color_name)
    logger.info("Setting the 'Highlight Color' to '%s'", closest_color_name)

    logger.debug(
        run(
            ["defaults", "write", "-g", "AppleAccentColor", "-int", str(closest_color.accent_color_id)],
            check=True,
        )
    )

    logger.debug(
        run(
            ["defaults", "write", "-g", "AppleHighlightColor", "-string", closest_color.highlight_color_id],
            check=True,
        )
    )

    if not parsed_args.skip_restart:
        logger.info(
            dedent(
                """
          Restarting Finder, Spotlight and System Preferences, others may need to be restarted manually
        """
            ).strip()
        )

        run(["killall", "Finder"], check=True)
        run(["killall", "Spotlight"], check=True)
        run(["osascript", "-e", 'tell application "System Preferences" to quit'], check=True)


def main():
    parser = get_args()

    parse_args(parser, sys.argv[1:])


if __name__ == "__main__":
    main()
