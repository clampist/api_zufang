import json
from toapi import Item, XPath

class GIO_DETAIL(Item):
    gio_detail_list = XPath('//div[@class="option-list sub-option-list gio_plate"]/a/@href')

    class Meta:
        source = None
        route = json.loads(open('route_list').read())
