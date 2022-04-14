import argparse
from asyncio import subprocess
import colors
from subprocess import run, PIPE

parser = argparse.ArgumentParser(
  description='Gets and sets the limited number of colors apple allows us',
  prog='osx-colors'
)

parser.add_argument('color', help='The source color in hex eg. 007aff leading # is optional')

# parser.add_argument('--output',
#     choices=['rgb','apple'],
#     default='rgb',
#     help='Output the color in RGB or Apples Internal Color Constant'
# )


# group = parser.add_mutually_exclusive_group()
# group.add_argument('-s', '--set', help='The source color in hex eg. 007aff leading # is optional', choices=['pink','red','blue'])
# group.add_argument('-c', '--set-custom', help='The source color in hex eg. 007aff leading # is optional', metavar='color')


args = parser.parse_args()

accent_color = colors.closest_accent_color_to(args.color)
highlight_color = colors.APPLE_HIGHLIGHT_COLORS[accent_color]

# print(f"Setting accent color to {accent_color}")
# print(f"Setting highlight color color to {highlight_color}")

cmd = ['defaults', 'write', '-g', 'AppleAccentColor', '-int', str(accent_color) ]
print(cmd)
print(run(cmd, stderr=PIPE, stdout=PIPE))

cmd = ['defaults', 'write', '-g', 'AppleHighlightColor', '-string', highlight_color ]
print(cmd)
run(cmd, stderr=PIPE, stdout=PIPE)
# crap = run(f'defaults write -g AppleAccentColor -int {accent_color}', stderr=PIPE, stdout=PIPE)
# print(crap)
# # killall Finder
# osascript -e 'tell application "System Preferences" to quit'
