import cadquery

class Part:
  def __init__(self, dimensions, volume_removed=None):
    self.dimensions = dimensions
    try:
      self.volume_removed = float(volume_removed) / 100.0
    except TypeError:
      self.volume_removed = 0.0

  def dimensions_str(self):
    return '_'.join([dimension.to_string() for dimension in self.dimensions.values()])

  def part_type(self):
    return "part"

  def to_string(self):
    return '_'.join([self.part_type(), self.dimensions_str(), "removed", str(self.volume_removed * 100)])

  def shape(self):
    return None

  def cadquery_object(self):
    return cadquery.build_object(self.shape())

  def to_step(self):
    return cadquery.exporters.toString(self.shape(), 'STEP')

  def export_step(self, fileLike):
    cadquery.exporters.exportShape(self.shape(), 'STEP', fileLike)
    fileLike.seek(0)
    return fileLike
