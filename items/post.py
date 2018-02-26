import json
from toapi import Item, XPath

class Post(Item):
    # title = XPath('//a[@class="js_triggerGray js_fanglist_title"]/@title')
    url = XPath('//a[@class="js_triggerGray js_fanglist_title"]/@href')
    # price_total = XPath('//div[@class="price"]/span/text()')
    # price_unit = XPath('//div[@class="price"]/text()[2]')
    one_room = XPath('//div[@class="where"]/span[1]/text()')
    room_pic = XPath('//img[@class="lj-lazy"]/@data-img-layout')

    class Meta:
        source = XPath('//ul[@class="house-lst js_fang_list"]/li')
        route = json.loads(open('post_route').read())
