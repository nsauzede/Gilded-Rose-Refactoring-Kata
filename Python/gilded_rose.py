class GildedRose:

    def __init__(self, name, days_remaining, quality):
        self.name = name
        self.days_remaining = days_remaining
        self.quality = quality

    def tick(self):
        match self.name:
            case "Normal Item":
                self.normal_tick()
            case "Aged Brie":
                self.brie_tick()
            case "Sulfuras, Hand of Ragnaros":
                self.sulfuras_tick()
            case "Backstage passes to a TAFKAL80ETC concert":
                self.backstage_tick()
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
        return # meh
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
