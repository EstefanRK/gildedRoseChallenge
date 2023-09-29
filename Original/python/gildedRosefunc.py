# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self, days):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
                and item.quality > 0
                and item.name != "Sulfuras, Hand of Ragnaros"
            ):
                item.quality -= 1
            else:
                if item.quality < 50:
                    item.quality += 1
                    if (
                        item.name == "Backstage passes to a TAFKAL80ETC concert"
                        and item.sell_in < 11
                        and item.quality < 50
                    ):
                        item.quality += 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality += 1

    def sellNthrow_items(self):
        thrown = []
        print("Sold items:")
        for item in self.items:
            if item.name != "Aged Brie":
                if item.quality > item.sell_in and item.sell_in > -1:
                    self.items.remove(item)
                    print(item)
                else:
                    thrown.append(item)

            # Sell Aged Brie if the sellin is equal to 0
            else:
                if item.sell_in == 0:
                    self.items.remove(item)
                    print(item)

        print("Thrown away:")
        if thrown != []:
            for item in thrown:
                print(item)
        else:
            print("Nothing was thrown away!")


# DON'T CHANGE----


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
