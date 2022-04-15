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

# NOTE: This is more of a placeholder at current to support potentially adding a
# read action or others and it also just looks plain weird without a verb after the commandline
parser.add_argument('action',
    choices=['set'],
    help='action to perform, only \'set\' is supported at current'
)
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

closest_color_name, closest_color = closest_colors_to(args.color)

logging.info("Searching for the closest Apple color to '%s' we found '%s'",
  args.color,
  closest_color_name
)

logging.info("Setting the 'Accent Color' to '%s'", closest_color_name)
logging.info("Setting the 'Highlight Color' to '%s'", closest_color_name)

logging.debug(
  run([
    'defaults', 'write', '-g', 'AppleAccentColor', '-int', str(closest_color.accent_color_id)],
    check=True
  )
)

logging.debug(
  run(
    ['defaults', 'write', '-g', 'AppleHighlightColor', '-string', closest_color.highlight_color_id ],
    check=True
  )
)

if not args.skip_restart:
    logging.info(dedent('''
      Restarting Finder, Spotlight and System Preferences, others may need to be restarted manually
    ''').strip())

    run(['killall', 'Finder'], check=True)
    run(['killall', 'Spotlight'], check=True)
    run(['osascript', '-e', 'tell application "System Preferences" to quit'], check=True)
