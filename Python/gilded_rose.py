from dataclasses import dataclass
@dataclass
class Item:
    quality:int; days_remaining:int
    def tick(self):pass
class Normal(Item):
    def tick(self):
        self.days_remaining -= 1
        if self.quality == 0:
            return
        self.quality -= 1
        if self.days_remaining <= 0:
            self.quality -= 1
class Brie(Item):
    def tick(self):
        self.days_remaining -= 1
        self.quality += 1
        if self.days_remaining <= 0:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50
class Backstage(Item):
    def tick(self):
        self.days_remaining -= 1
        if self.quality >= 50:
            return
        if self.days_remaining < 0:
            self.quality = 0
            return
        self.quality += 1
        if self.days_remaining < 10:
            self.quality += 1
        if self.days_remaining < 5:
            self.quality += 1
def GildedRose(name, days_remaining, quality):
    return Normal(quality, days_remaining) if name == "Normal Item" else \
        Brie(quality, days_remaining) if name == "Aged Brie" else \
        Backstage(quality, days_remaining) if name == "Backstage passes to a TAFKAL80ETC concert" else \
        Item(quality, days_remaining)
