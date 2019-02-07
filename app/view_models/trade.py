"""
Created by Oort on 2018/12/6 3:06 PM.
主要作用礼物与心愿清单的列表
"""
from collections import namedtuple

__author__ = 'Oort'

# 我的礼物模型
from app.view_models.book import BookViewModel


class TradeInfo:

    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )


MyTrade = namedtuple("MyTrade", ['id', 'book', 'count'])


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []
        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trad in self.__trades_of_mine:
            temp_trades.append(self.__matching(trad))
        return temp_trades

    def __matching(self, trad):
        count = 0
        for EachGiftWishCount in self.__trade_count_list:
            if trad.isbn == EachGiftWishCount.isbn:
                count = EachGiftWishCount.count
        my_trad = MyTrade(trad.id, BookViewModel(trad.book), count)
        return my_trad
