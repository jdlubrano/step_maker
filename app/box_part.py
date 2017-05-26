from cadquery import Workplane

from part import Part

class BoxPart(Part):
  @staticmethod
  def dimensions():
    return ['length', 'width', 'thickness']

  def box(self):
    return Workplane("XY").box(self.dimensions['length'],
                               self.dimensions['width'],
                               self.dimensions['thickness'])

  def shape(self):
    return self.box()
