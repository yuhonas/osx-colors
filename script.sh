#!/usr/bin/env zsh

# source ~/.zprofile

source_color=$(cat ~/.cache/wal/colors.json  | jq --raw-output '.colors.color4')
apple_color=$(python ~/Sites/pywal-macos-accent-colors/src/commandline.py --output apple $source_color)

echo $source_color
echo $apple_color

defaults write -g AppleAccentColor -int $apple_color
killall Finder
osascript -e 'tell application "System Preferences" to quit'
