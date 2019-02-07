from collections import namedtuple

# 我的礼物模型
from app.view_models.book import BookViewModel
from app.view_models.trade import MyTrades


class MyWishs(MyTrades):

    def __init__(self, trades_of_mine, trade_count_list):
        super(MyWishs, self).__init__(trades_of_mine, trade_count_list)
