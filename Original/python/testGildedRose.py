# -*- coding: utf-8 -*-
import unittest

from gildedRosefunc import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gildedRosefunc = GildedRose(items)
        gildedRosefunc.update_quality()
        GildedRose(items).sellNthrow_items()
        self.assertEquals("foo", items[0].name)


if __name__ == "__main__":
    unittest.main()
