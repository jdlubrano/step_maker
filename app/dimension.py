class Dimension:
  CONVERSION_FACTORS = { 'in': 25.4, 'cm': 10, 'mm': 1 }

  def __init__(self, value, units):
    self.value = float(value)
    self.units = units

  def to_string(self):
    return str(self.value) + self.units

  def in_mm(self):
    return Dimension.CONVERSION_FACTORS[self.units] * self.value
