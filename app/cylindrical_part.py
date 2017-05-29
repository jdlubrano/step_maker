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

  def cylinder(self):
    return Workplane("XY").circle(self.diameter() / 2) \
            .extrude(self.length())

  def shape(self):
    return self.cylinder()
