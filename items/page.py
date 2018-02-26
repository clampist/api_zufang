import json
from toapi import Item, XPath

class Page(Item):
    next_page = XPath('//a[@gahref="results_next_page"]/@href')

    class Meta:
        source = None
        route = json.loads(open('post_route').read())
