from toapi import Api
from items.page import Page
from items.post import Post
from items.gio_district import GIO
from items.gio_detail import GIO_DETAIL

from settings import MySettings

api = Api('http://sh.lianjia.com', settings=MySettings)
api.register(Page)
api.register(Post)
api.register(GIO)
api.register(GIO_DETAIL)

if __name__ == '__main__':
    api.serve()
