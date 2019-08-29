import scrapy
from rent.items import RentItem
from datetime import datetime
import re


class Rent(scrapy.Spider):
	name = "rent_scraper"

	# First Start Url
	start_urls = ["https://dom.ria.com/uk/arenda-kvartir/kiev/"]

	npages = 281

	# This mimics getting the pages using the next button. 
	for i in range(2, npages):
		start_urls.append("https://dom.ria.com/uk/arenda-kvartir/kiev/?page="+str(i)+"")

	def parse(self, response):
		for href in response.xpath("//a[@class='blue']/@href"):
			# add the scheme, eg http://
			url  = "https://dom.ria.com" + href.extract() 
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = RentItem()

		item['ID'] = response.xpath("//strong/text()").extract()[0]

		item['Price'] = response.xpath("//span[@class='price']/text()").extract()[0].strip()

		item['Adress'] = response.xpath("//h1[@class='head']/text()").extract()

		list1 = response.xpath("//span[@class='label']/text()").extract()
		del list1[0]

		list2 = response.xpath("//span[@class='argument']/text()").extract()

		item['Rooms'] = list2[list1.index('Кімнат:')].strip()

		item['Floor'] = list2[list1.index('Поверх:')].strip()

		item['TotalFloor'] = list2[list1.index('Поверховість:')].strip()

		try:
			item['TotalArea'] = list2[list1.index('Загальна:')]
		except: 
			item['TotalArea'] = float('nan')

		try:
			item['LivingArea'] = list2[list1.index('Житлова:')]
		except:
			item['LivingArea'] = float('nan')

		try:
			item['KitchenArea'] = list2[list1.index('Кухня:')]
		except:
			item['KitchenArea'] = float('nan')

		try:
			item['AdPrice'] = list2[list1.index('Додаткові платежі:')]
		except:
			item['AdPrice'] = float('nan')

		try:
			item['OfferType'] = list2[list1.index('Тип пропозиції:')]
		except:
			item['OfferType'] = float('nan')

		try:
			item['Walls'] = list2[list1.index('Тип стін:')]
		except:
			item['Walls'] = float('nan')

		list3 = response.xpath("//dt/text()").extract()

		if 'до центра міста:' in list3:
			item['Center'] = True
		else:
			item['Center'] = False

		if 'школа:' in list3:
			item['School'] = True
		else:
			item['School'] = False

		if 'дитячий садок:' in list3:
			item['Kindergarten'] = True
		else:
			item['Kindergarten'] = False

		if 'лікарня:' in list3:
			item['Hospital'] = True
		else:
			item['Hospital'] = False

		list4 = response.xpath("//span[@class='grey']/text()").extract()

		if 'бойлер' in list4:
			item['WaterHeatType'] = True
		else:
			item['WaterHeatType'] = False

		item['Rate'] = float('nan')

		item['Street'] = float('nan')

		item['District'] = float('nan')

		item['Metro'] = float('nan')

		yield item







