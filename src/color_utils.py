from colorsys import rgb_to_hsv

APPLE_BLUE=4
APPLE_PURPLE=5
APPLE_PINK=6
APPLE_RED=0
APPLE_ORANGE=1
APPLE_YELLOW=2
APPLE_GREEN=3
APPLE_GRAPHITE="-1"

# AppleAccentColor
APPLE_ACCENT_COLORS = {
  (0, 122, 255): APPLE_BLUE,
  (165, 80, 167): APPLE_PURPLE,
  (247, 79, 158): APPLE_PINK,
  (255, 82, 87): APPLE_RED,
  (247, 130, 27): APPLE_ORANGE,
  (255, 198, 0): APPLE_YELLOW,
  (98, 186, 70): APPLE_GREEN,
  (140, 140, 140): APPLE_GRAPHITE,
}

# AppleHighlightColor
APPLE_HIGHLIGHT_COLORS = {
  APPLE_BLUE: "0.698039 0.843137 1.000000 Blue",
  APPLE_PURPLE: "0.968627 0.831373 1.000000 Purple",
  APPLE_PINK: "1.000000 0.749020 0.823529 Pink",
  APPLE_RED: "1.000000 0.733333 0.721569 Red",
  APPLE_ORANGE: "1.000000 0.874510 0.701961 Orange",
  APPLE_YELLOW: "1.000000 0.937255 0.690196 Yellow",
  APPLE_GREEN: "0.752941 0.964706 0.678431 Green",
  APPLE_GRAPHITE: "0.847059 0.847059 0.862745 Graphite"
}

def hex_to_rgb(color):
    """ converts hex color to rgb """
    color = color.lstrip('#')
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def to_hsv( color ):
    """ converts color tuples to floats and then to hsv """
    return rgb_to_hsv(*[x/255.0 for x in color]) #rgb_to_hsv wants floats!

def color_dist( color1, color2):
    """ returns the squared euklidian distance between two color vectors in hsv space """
    return sum( (a-b)**2 for a,b in zip(to_hsv(color1),to_hsv(color2)) )

def min_color_diff( color_to_match, colors):
    """ returns the `(distance, color_name)` with the minimal distance to `colors`"""
    color_distances = (
        (color_dist(color_to_match, test), colors[test]) # (distance to `test` color, color name)
        for test in colors)

    return min(color_distances)

def closest_colors_to(color):
    """ returns the closest apple accent color to the one provided """
    closest_apple_color = min_color_diff(hex_to_rgb(color), APPLE_ACCENT_COLORS)[1]

    return((closest_apple_color, APPLE_HIGHLIGHT_COLORS[closest_apple_color]))
