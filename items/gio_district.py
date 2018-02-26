import json
from toapi import Item, XPath

class GIO(Item):
    gio_list = XPath('//div[@class="option-list gio_district"]/a/@href')

    class Meta:
        source = None
        route = {
                '/zufang/':'/zufang/',
                }
