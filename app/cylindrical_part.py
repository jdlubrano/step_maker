from math import sqrt
from cadquery import Workplane

from part import Part

class CylindricalPart(Part):
  @staticmethod
  def dimensions():
    return ['length', 'diameter']

  def part_type(self):
    return "cylindrical"

  def length(self):
    return self.dimensions['length'].in_mm()

  def diameter(self):
    return self.dimensions['diameter'].in_mm()

  def radius(self):
    return self.diameter() / 2

  def hole_radius(self):
    return self.radius() * sqrt(self.volume_removed)

  def hole_diameter(self):
    return 2 * self.hole_radius()

  def cylinder(self):
    return Workplane("XY").circle(self.diameter() / 2) \
            .extrude(self.length())

  def cylinder_with_hole(self):
    return self.cylinder().faces(">Z").workplane().hole(self.hole_diameter())

  def shape(self):
    return self.cylinder_with_hole()
