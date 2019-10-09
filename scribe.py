#!/usr/bin/env python3

"""
scribe.py -- Simple Python APIs for programmatically creating drawings.

"""

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
        pass

    def __repr__(self):
        """
        Friendly string representation.

        """
        pass

    @property
    def foreground_color(self):
        """
        Returns the foreground color as a 4-tuple containing the red, green,
        blue, and alpha values.

        """
        pass

    @foreground_color.setter
    def foreground_color(self, color):
        """
        Sets the foreground color to `color`. `color` is a 4-tuple containing
        the red, green, blue, and alpha values.

        """
        pass

    @property
    def background_color(self):
        """
        Returns the background color as a 4-tuple containing the red, green,
        blue, and alpha values.

        """
        pass

    @background_color.setter
    def background_color(self, color):
        """
        Sets the background color to `color`. `color` is a 4-tuple containing
        the red, green, blue, and alpha values.

        """
        pass

    @property
    def stroke_width(self):
        """
        Returns the stroke width.

        """
        pass

    @stroke_width.setter
    def stroke_width(self, width):
        """
        Sets the stroke width to `width`.

        """
        pass


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
