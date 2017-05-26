from cadquery import Workplane

from part import Part

class RectangularPart(Part):
  @staticmethod
  def dimensions():
    return ['length', 'width', 'thickness']

  def part_type(self):
    return "rectangular"

  def box(self):
    return Workplane("XY").box(self.dimensions['length'].in_mm(), # x
                               self.dimensions['width'].in_mm(), # y
                               self.dimensions['thickness'].in_mm()) # z

  def shape(self):
    return self.box()
