class GildedRose:

    def __init__(self, name, days_remaining, quality):
        self.name = name
        self.days_remaining = days_remaining
        self.quality = quality

    def tick(self):
        match self.name:
            case "Normal Item":
                return self.normal_tick()
            case "Aged Brie":
                return self.brie_tick()
            case "Sulfuras, Hand of Ragnaros":
                return self.sulfuras_tick()
            case "Backstage passes to a TAFKAL80ETC concert":
                return self.backstage_tick()
        if self.name != "Aged Brie" and self.name != "Backstage passes to a TAFKAL80ETC concert":
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.name == "Backstage passes to a TAFKAL80ETC concert":
                    if self.days_remaining < 11:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.days_remaining < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.days_remaining = self.days_remaining - 1
        if self.days_remaining < 0:
            if self.name != "Aged Brie":
                if self.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.quality > 0:
                        if self.name != "Sulfuras, Hand of Ragnaros":
                            self.quality = self.quality - 1
                else:
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
    def backstage_tick(self):
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
    def sulfuras_tick(self):
        return
    def brie_tick(self):
        self.days_remaining -= 1
        self.quality += 1
        if self.days_remaining <= 0:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50
    def normal_tick(self):
        self.days_remaining -= 1
        if self.quality == 0:
            return
        self.quality -= 1
        if self.days_remaining <= 0:
            self.quality -= 1
