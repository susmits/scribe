#!/usr/bin/env python3

"""
scribe.py -- Simple Python APIs for programmatically creating drawings.

"""

import collections
import xml.etree.ElementTree as ET

##############################################################################
## Helper functions.
##

def to_color_tuple(color):
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


def stringize_values(dict):
    """
    Returns the dict, made of the same keys but stringized values.

    """
    stringized_dict = {}
    for k, v in dict.items():
        stringized_dict[k] = str(v)
    return stringized_dict


def to_svg_color(color_tuple):
    """
    Converts a 4-tuple containing red, green, blue, and alpha values to an
    SVG #RGBA color code.

    """
    return "#%02x%02x%02x%02x" % color_tuple


def add_paint(shape_tag, paint):
    """
    Add the specified paint to the given SVG shape tag.

    """
    paint_attrib = stringize_values({
        "stroke"      : to_svg_color(paint.foreground_color),
        "fill"        : to_svg_color(paint.background_color),
        "stroke-width": paint.stroke_width,
    })
    shape_tag.attrib.update(paint_attrib)
    return shape_tag


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
        self._foreground_color = to_color_tuple(color)

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
        self._background_color = to_color_tuple(color)

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
        self._width = width
        self._height = height
        self._paint = Paint()
        self._shape_list = collections.OrderedDict()
        self._next_shape_id = 1

    @property
    def width(self):
        """
        Returns the width of the canvas.

        """
        return self._width
    
    @property
    def height(self):
        """
        Returns the height of the canvas.

        """
        return self._height

    @property
    def paint(self):
        """
        Returns the paint currently associated with this canvas.

        """
        return self._paint

    @paint.setter
    def paint(self, p):
        """
        Sets the paint for the canvas to `p`.

        """
        self._paint = p

    def convert_to_svg(self):
        """
        Returns the contents of this canvas as an SVG ElementTree.

        """
        svg_root = ET.Element("svg",
            {
                "viewbox": f"0 0 {self.width} {self.height}",
                "xmlns": "http://www.w3.org/2000/svg",
            })

        for shape in self._shape_list.values():
            # Unpack.
            shape_type, *args = shape
            shape_tag = None
            
            if shape_type == "line":
                attribs = stringize_values({
                    "x1": args[0],
                    "y1": args[1],
                    "x2": args[2],
                    "y2": args[3],
                })
                shape_tag = ET.Element("line", attribs)
            elif shape_type == "circle":
                attribs = stringize_values({
                    "cx": args[0],
                    "cy": args[1],
                    "r" : args[2],
                })
                shape_tag = ET.Element("circle", attribs)
            elif shape_type == "rect":
                attribs = stringize_values({
                    "x"     : args[0],
                    "y"     : args[1],
                    "width" : args[2] - args[0],
                    "height": args[3] - args[1],
                })
                shape_tag = ET.Element("rect", attribs)

            add_paint(shape_tag, args[-1])
            svg_root.append(shape_tag)

        svg = ET.ElementTree(svg_root)
        return svg

    def draw_line(self, start_x, start_y, end_x, end_y, paint=None):
        """
        Draws a line from (`start_x`, `start_y`) to (`end_x`, `end_y`). If
        a paint isn't specified, the paint associated with the canvas is
        used.

        """
        if paint is None:
            paint = self._paint
    
        shape = ("line", start_x, start_y, end_x, end_y, paint)
        return self._add_shape_to_store(shape)

    def draw_circle(self, center_x, center_y, radius, paint=None):
        """
        Draws a circle centered at (`center_x`, `center_y`) with the specified
        radius. If a paint isn't specified, the paint associated with the
        canvas is used.

        """
        if paint is None:
            paint = self._paint
    
        shape = ("circle", center_x, center_y, radius, paint)
        return self._add_shape_to_store(shape)

    def draw_rectangle(self, left, top, right, bottom, paint=None):
        """
        Draws a rectangle from (`left`, `top`) to (`right`, `bottom`). If a
        paint isn't specified, the paint associated with the canvas is used.

        """
        if paint is None:
            paint = self._paint
    
        shape = ("rect", left, top, right, bottom, paint)
        return self._add_shape_to_store(shape)

    def _add_shape_to_store(self, shape):
        """
        Internal function that adds the specified shape to the shape list
        and returns its key.

        """
        shape_id = self._next_shape_id
        self._next_shape_id += 1

        self._shape_list[shape_id] = shape
        return shape_id 


##############################################################################
