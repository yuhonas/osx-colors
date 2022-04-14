import argparse
from asyncio import subprocess
from re import I
from .colors import closest_colors_to
from subprocess import run, PIPE

parser = argparse.ArgumentParser(
  description='Gets and sets the limited number of colors apple allows us',
  prog='osx-colors'
)

parser.add_argument('color', help='The color to set in hex eg. 007aff leading # is optional')
parser.add_argument('-r','--restart', action="store_true", help='Restart Finder and System Preferences after setting')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

# group = parser.add_mutually_exclusive_group()
# group.add_argument('-s', '--set', help='The source color in hex eg. 007aff leading # is optional', choices=['pink','red','blue'])
# group.add_argument('-c', '--set-custom', help='The source color in hex eg. 007aff leading # is optional', metavar='color')

args = parser.parse_args()

print(args)

accent_color, highlight_color = closest_colors_to(args.color)

cmd = ['defaults', 'write', '-g', 'AppleAccentColor', '-int', str(accent_color) ]
print(cmd)
print(run(cmd, stderr=PIPE, stdout=PIPE))

cmd = ['defaults', 'write', '-g', 'AppleHighlightColor', '-string', highlight_color ]
print(cmd)
run(cmd, stderr=PIPE, stdout=PIPE)

if(args.restart):
    print(run(['killall', 'Finder']))
    print(run(['osascript', '-e', 'tell application "System Preferences" to quit']))
