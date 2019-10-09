#!/usr/bin/env python3

"""
scribe.py -- Simple Python APIs for programmatically creating drawings.

"""

##############################################################################
## Helper functions.
##

def to_rgba(color):
    """
    Converts `color` to a 4-tuple containing red, green, blue, and alpha
    values.

    """
    rgba = tuple(color)
    is_valid_color_component = lambda x: type(x) is int and 0 <= x <= 255
    if len(rgba) == 4 and all(map(is_valid_color_component, color)):
        return rgba
    else:
        raise ValueError(f"{color} is not a valid RGBA 4-tuple.")


##############################################################################
## Paint.
##

class Paint(object):
    """
    Paint class. This describes the paint.

    """
    def __init__(self):
        """
        Initializes a blank Paint instance.

        """
        self._foreground_color = (0, 0, 0, 0)
        self._background_color = (0, 0, 0, 0)
        self._stroke_width = 0.0

    def __repr__(self):
        """
        Friendly string representation.

        """
        return f"<paint fg {self._foreground_color} bg {self._background_color} " \
            f"stroke {self._stroke_width}>"

    @property
    def foreground_color(self):
        """
        Returns the foreground color as a 4-tuple containing the red, green,
        blue, and alpha values.

        """
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, color):
        """
        Sets the foreground color to `color`. `color` is a 4-tuple containing
        the red, green, blue, and alpha values.

        """
        self._foreground_color = to_rgba(color)

    @property
    def background_color(self):
        """
        Returns the background color as a 4-tuple containing the red, green,
        blue, and alpha values.

        """
        return self._background_color

    @background_color.setter
    def background_color(self, color):
        """
        Sets the background color to `color`. `color` is a 4-tuple containing
        the red, green, blue, and alpha values.

        """
        self._background_color = to_rgba(color)

    @property
    def stroke_width(self):
        """
        Returns the stroke width.

        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, width):
        """
        Sets the stroke width to `width`.

        """
        self._stroke_width = float(width)


##############################################################################
## Canvas.
##

class Canvas(object):
    """
    Canvas class. Use this to accumulate drawn shapes.

    """
    def __init__(self, width, height):
        """
        Initializes a canvas with the specified width and height.

        """
        pass

    @property
    def paint(self):
        """
        Returns the paint currently associated with this canvas.

        """
        pass

    @paint.setter
    def paint(self, p):
        """
        Sets the paint for the canvas to `p`.

        """
        pass

    def draw_line(self, start_x, start_y, end_x, end_y, paint=None):
        """
        Draws a line from (`start_x`, `start_y`) to (`end_x`, `end_y`). If
        a paint isn't specified, the paint associated with the canvas is
        used.

        """
        pass

    def draw_circle(self, center_x, center_y, radius, paint=None):
        """
        Draws a circle centered at (`center_x`, `center_y`) with the specified
        radius. If a paint isn't specified, the paint associated with the
        canvas is used.

        """
        pass

    def draw_rectangle(self, left, top, right, bottom, paint=None):
        """
        Draws a rectangle from (`left`, `top`) to (`right`, `bottom`). If a
        paint isn't specified, the paint associated with the canvas is used.

        """
        pass


##############################################################################
## Save to a file.
##

def write_svg(file_like_obj, canvas):
    """
    Writes the shapes drawn on `canvas` into `file_like_obj`, which is a file
    or file like object.

    """
    pass


##############################################################################
