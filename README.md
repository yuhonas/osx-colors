# osx-colors [![ci](https://github.com/yuhonas/osx-colors/workflows/ci/badge.svg)](https://github.com/yuhonas/osx-colors/actions/workflows/ci.yml)

Sane command line color customisation for osx, no more fiddling about with `defaults`, internal apple color constants and rgb color codes

Say you want to change your Accent/Highlight Color to Green like this

![](./osx-general-preference-pane.jpg)


If you wanted to change it via terminal, normally you'd need to do this

```
$ defaults write -g AppleAccentColor -string 3
$ defaults write -g AppleHighlightColor -string "0.752941 0.964706 0.678431 Green"
```

Instead.... do this 😄

```
$ osx-colors set green
```

## Features

* Sane color handling using color names
* When provided a color in hex it'll find the "nearest" available apple color to it
and set it to this, this is awesome if you use [pywal](https://github.com/dylanaraps/pywal) and want matching accent/highlight colors to your wallpaper
* Restarts Finder,Docker,System Preferences etc upon setting so colors can be immediately seen

## Why

I'm a huge fan of [pywal](https://github.com/dylanaraps/pywal) and what I thought would really be the cherry on
top would be Accent/Highlight colors that were based on the color palette of the wallaper, however I wasn't able
to find anything that did it and color management from the commandline simply sucked, so I wrote this for my personal needs

## Limitations

At present you can only set both the `AccentColor` and `HighlightColor` together, however the `HighlightColor`
can be customized to any color in the UI (from what I can see)

## Getting Started

### Dependencies

* MacOS Monterey (It probably works on others I just haven't tested it!)
* Python 3.8 or greater

### Installing

TBD

## License

This project is licensed under the MIT license

## Acknowledgments

* Thanks to [ofstack](https://ofstack.com/python/11731/python-implements-a-method-to-find-the-closest-approximation-to-a-given-color-from-a-set-of-colors.html) for the code to match the "nearest" color, i'm no color scientist
* Thanks to [quantum_libet](https://www.reddit.com/r/MacOS/comments/boju0v/cant_change_accent_color_in_mojave_terminal/) on reddit for a rundown on the insanity of color management via the terminal
