import pdb
import cadquery

class Part:
  def __init__(self, dimensions, volume_removed=0):
    self.dimensions = dimensions
    self.volume_removed = volume_removed

  def shape(self):
    return None

  def cadquery_object(self):
    return cadquery.build_object(self.shape())

  def to_step(self):
    return cadquery.exporters.toString(self.shape(), 'STEP')

  def export_step(self, fileLike):
    cadquery.exporters.exportShape(self.shape(), 'STEP', fileLike)
