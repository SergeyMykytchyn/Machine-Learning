# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RentItem(scrapy.Item):
    ID = scrapy.Field()
    Price = scrapy.Field()
    Adress = scrapy.Field()
    Rooms = scrapy.Field()
    Floor = scrapy.Field()
    TotalFloor = scrapy.Field()
    TotalArea = scrapy.Field()
    LivingArea = scrapy.Field()
    KitchenArea = scrapy.Field()
    AdPrice = scrapy.Field()
    OfferType = scrapy.Field()
    Walls = scrapy.Field()
    Center = scrapy.Field()
    School = scrapy.Field()
    Kindergarten = scrapy.Field()
    Hospital = scrapy.Field()
    WaterHeatType = scrapy.Field()
    Rate = scrapy.Field()
    Street = scrapy.Field()
    District = scrapy.Field()
    Metro = scrapy.Field()

