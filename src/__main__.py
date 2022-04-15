import argparse
from subprocess import run
import logging
from textwrap import dedent

from .color_utils import closest_colors_to
from . import settings

logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger()

parser = argparse.ArgumentParser(
  description='Sets the limited number of colors apple allows us too',
  prog=settings.get_app_name(),
  formatter_class=argparse.RawDescriptionHelpFormatter,
  epilog=dedent(f'''
    Example:
    # To set osx to use Apple Green
    $ {settings.get_app_name()} set 62ba46
  ''')
)

parser.add_argument('action', choices=['set'], help='action to perform')
parser.add_argument('color', help='color to set in hex eg. 007aff leading # is optional')
parser.add_argument('-s','--skip-restart',
    action="store_true",
    help='skip restarting Finder, Spotlight and System Preferences'
)
parser.add_argument('-v', '--version',
    action='version',
    version=f'%(prog)s {settings.get_version()}'
)

args = parser.parse_args()

accent_color, highlight_color = closest_colors_to(args.color)

logging.info("Setting the 'Accent Color' to the closest color to '%s'", args.color)
logging.info("Setting the 'Highlight Color' to the closest color to '%s'", args.color)

logging.debug(
  run(['defaults', 'write', '-g', 'AppleAccentColor', '-int', str(accent_color)], check=True)
)

logging.debug(
  run(['defaults', 'write', '-g', 'AppleHighlightColor', '-string', highlight_color ], check=True)
)

if not args.skip_restart:
    logging.info(dedent('''
      Restarting Finder, Spotlight and System Preferences, others may need to be restarted manually
    ''').strip())

    run(['killall', 'Finder'], check=True)
    run(['killall', 'Spotlight'], check=True)
    run(['osascript', '-e', 'tell application "System Preferences" to quit'], check=True)
