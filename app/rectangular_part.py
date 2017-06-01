from math import ceil
from math import pi
from math import sqrt
from cadquery import Workplane

from part import Part

class RectangularPart(Part):
  @staticmethod
  def dimensions():
    return ['length', 'width', 'thickness']

  def part_type(self):
    return "rectangular"

  def length(self):
    return self.dimensions['length'].in_mm()

  def width(self):
    return self.dimensions['width'].in_mm()

  def area_removed(self):
    return self.length() * self.width() * self.volume_removed

  def total_radius(self):
    return sqrt(self.area_removed() / pi)

  def max_radius(self):
    return min(self.length() / 2, self.width() / 2, self.total_radius())

  def number_of_holes(self):
    return int(ceil(self.area_removed() / (self.max_radius()**2 * pi)))

  def hole_radius(self):
    return self.total_radius() / sqrt(self.number_of_holes())

  def hole_diameter(self):
    return 2 * self.hole_radius()

  def box(self):
    return Workplane("XY").box(self.length(), # x
                               self.width(), # y
                               self.dimensions['thickness'].in_mm()) # z

  def holes_along_y(self):
    negative_y = -self.width() / 2
    distance_between = self.width() / (self.number_of_holes() + 1)
    return [(0, (i + 1) * distance_between + negative_y) for i in range(self.number_of_holes())]

  def holes_along_x(self):
    negative_x = -self.length() / 2
    distance_between = self.length() / (self.number_of_holes() + 1)
    return [((i + 1) * distance_between + negative_x, 0) for i in range(self.number_of_holes())]

  def hole_locations(self):
    return self.holes_along_x() if self.length() >= self.width() else self.holes_along_y()

  def box_with_holes(self):
    return self.box().faces(">Z").workplane().pushPoints(self.hole_locations()).hole(self.hole_diameter())

  def shape(self):
    return self.box_with_holes() if self.volume_removed > 0 else self.box()
