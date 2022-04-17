from colorsys import rgb_to_hsv
from collections import namedtuple

AppleColor = namedtuple("AppleColor", "rgb accent_color_id highlight_color_id")

APPLE_COLORS = {
    "blue": AppleColor((0, 122, 255), 4, "0.698039 0.843137 1.000000 Blue"),
    "purple": AppleColor((165, 80, 167), 5, "0.968627 0.831373 1.000000 Purple"),
    "pink": AppleColor((247, 79, 158), 6, "1.000000 0.749020 0.823529 Pink"),
    "red": AppleColor((255, 82, 87), 0, "1.000000 0.733333 0.721569 Red"),
    "orange": AppleColor((247, 130, 27), 1, "1.000000 0.874510 0.701961 Orange"),
    "yellow": AppleColor((255, 198, 0), 2, "1.000000 0.937255 0.690196 Yellow"),
    "green": AppleColor((98, 186, 70), 3, "0.752941 0.964706 0.678431 Green"),
    "graphite": AppleColor((140, 140, 140), "-1", "0.847059 0.847059 0.862745 Graphite"),
}


def hex_to_rgb(color):
    """converts hex color to rgb"""
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))


def to_hsv(color):
    """converts color tuples to floats and then to hsv"""
    return rgb_to_hsv(*[x / 255.0 for x in color])  # rgb_to_hsv wants floats!


def color_dist(color1, color2):
    """returns the squared euklidian distance between two color vectors in hsv space"""
    return sum((a - b) ** 2 for a, b in zip(to_hsv(color1), to_hsv(color2)))


def min_color_diff(color_to_match, colors):
    """returns the `(distance, color_name)` with the minimal distance to `colors`"""
    color_distances = (
        (
            color_dist(color_to_match, apple_color.rgb),
            color_name,
        )
        for color_name, apple_color in colors.items()
    )

    return min(color_distances)


def closest_colors_to(color):
    """returns the closest apple accent color to the one provided"""
    closest_apple_color_name = min_color_diff(hex_to_rgb(color), APPLE_COLORS)[1]

    return (closest_apple_color_name, APPLE_COLORS[closest_apple_color_name])
