from app.view_models.trade import MyTrades


class MyGifts(MyTrades):

    def __init__(self, trades_of_mine, trade_count_list):
        super(MyGifts, self).__init__(trades_of_mine, trade_count_list)
