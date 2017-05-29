from math import pi
from math import sqrt

import unittest

from app.dimension import Dimension
from app.rectangular_part import RectangularPart

class RectangularPartTest(unittest.TestCase):
  def dimensions(self, length=5, width=1, thickness=0.25):
    return {
      'length': Dimension(length, 'mm'),
      'width': Dimension(width, 'mm'),
      'thickness': Dimension(thickness, 'mm')
    }

  def part(self, dimensions, vol_removed=0):
    return RectangularPart(dimensions, vol_removed)

  def default_part(self, vol_removed=0):
    return RectangularPart(self.dimensions(), vol_removed)

  def test_sanity(self):
    assert(True)

  def test_length(self):
    self.assertEqual(self.default_part().length(), 5)

  def test_area_removed(self):
    self.assertEqual(self.default_part().area_removed(), 0)
    self.assertEqual(self.default_part(20).area_removed(), 1)
    self.assertEqual(self.part(self.dimensions(5, 5), 20).area_removed(), 5)

  def test_max_radius(self):
    # When width is the short dimension
    self.assertEqual(self.default_part(20).max_radius(), 0.5)
    # When length is the short dimension
    self.assertEqual(self.part(self.dimensions(1, 5), 20).max_radius(), 0.5)
    # When the volume can be removed in 1 hole
    self.assertEqual(
      self.part(self.dimensions(5, 5), 20).max_radius(),
      sqrt(5 / pi))

  def test_number_of_holes(self):
    self.assertEqual(self.default_part(10).number_of_holes(), 1)
    self.assertEqual(self.default_part(20).number_of_holes(), 2)
    self.assertEqual(self.part(self.dimensions(2, 8), 40).number_of_holes(), 3)

  def test_hole_radius(self):
    self.assertEqual(self.default_part(10).hole_radius(), sqrt(0.5 / pi))
    self.assertAlmostEqual(self.default_part(20).hole_radius(), sqrt(0.5 / pi))

  def test_holes_along_x(self):
    self.assertEqual(
      self.part(self.dimensions(6), 20).holes_along_x(),
      [(-1, 0), (1, 0)])

    self.assertEqual(
      self.part(self.dimensions(8, 2), 40).holes_along_x(),
      [(-2, 0), (0, 0), (2, 0)])

  def test_holes_along_y(self):
    self.assertEqual(
      self.part(self.dimensions(1, 6), 20).holes_along_y(),
      [(0, -1), (0, 1)])

    self.assertEqual(
      self.part(self.dimensions(2, 8), 40).holes_along_y(),
      [(0, -2), (0, 0), (0, 2)])
