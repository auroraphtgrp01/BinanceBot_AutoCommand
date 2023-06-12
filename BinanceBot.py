import ccxt
import time
# exchange = ccxt.binance({
#     'apiKey': 'IGDKTUg929EQ91wXyQ1eyc3U5jIDXoKtkdajL7Vc6CVIcriMFDP4WEpPi611lqAI',
#     'secret': 'rxcpcXxM7enU9d9gWx8YuJev0xOrLXlCOenovWn6Qxd3u0T6frUPt9t3fLtJKIkP',
#     'enableRateLimit': True
#     })
exchange = ccxt.binance({
    'apiKey': 'GLvzWZNUtNCoev8GBPxqcOavNu3g6XG285IY92KmlzPqU6I7CcgogsPzTDsz5KeU',
    'secret': 'yWZLKFIdA0vcrynQjQHE84dD8ryF0RWv7iDvMnjCLm5zYnBm0JhoKQLIUy7JvXJ8',
    'enableRateLimit': True
    })
#------------------------------------------------------------------------------------------------------------------------------
# LIMIT_COMMAND
def setCommandBuyLimit(symbol_call):
    print("--------------------------------------------------------------------------------------------------------------")
    print("Nhận lệnh - Đang tiến hành đặt lệnh ")
    print("Tiến hành đặt lệnh mua "+str(symbol_call))
    balance = exchange.fetch_balance()
    usdt_balance = balance['total']['USDT']
# Đặt thông tin giao dịch
    symbol = symbol_call  # Cặp giao dịch BTC/USDT
    ticker = exchange.fetch_ticker(symbol_call)
    last_price = ticker['last']
    print("Giá Hiện Tại Của "+str(symbol_call)+" là: "+str(last_price))
    amount = (usdt_balance/last_price) - (usdt_balance/last_price)*0.05   # Số lượng coin BTC muốn mua
    limit_price = last_price # Giá limit mua
    
# Kiểm tra sẵn sàng giao dịch
    exchange.load_markets()
    if symbol in exchange.markets:
        market = exchange.markets[symbol]
        if market['active']:
            print('Sàn giao dịch và cặp giao dịch đã sẵn sàng.')
        # Kiểm tra số dư USDT
            if usdt_balance >= (amount * limit_price):
                print(f'Số dư USDT đủ ({usdt_balance}) để thực hiện giao dịch.')
                price_After=0
# ------------------------------------------------------------------------------------------------------------------------
                # ORDER_MARKET_BUY
                # order = exchange.create_limit_buy_order(symbol, amount, limit_price)
                # try:
                #     market_buy = exchange.create_market_buy_order(symbol_call, amount)
                #     price_After = currentPrice(symbol_call)
                #     print("Lệnh mua thành công!")
                # except ccxt.ExchangeError as e:
                #     print("Lỗi khi thực hiện lệnh mua:", e)
                # print('Giao dịch đã được thực hiện.')
# ------------------------------------------------------------------------------------------------------------------------
                try:
                    order = exchange.create_limit_buy_order(symbol, amount, last_price)
                    order_id = order['id']
                    print("Order ID của lệnh là: "+str(order_id))
                except ccxt.ExchangeError as e:
                    print("Lỗi khi đặt lệnh giới hạn mua:", e)
                print("---------------------------- KIỂM TRA KHỚP LỆNH LIMIT ----------------------------------------------------------")
                while(True):
                    if(check_limit_buy(symbol)):
                        ticker = exchange.fetch_ticker(symbol_call)
                        last_price = ticker['last']
                        price_After = last_price
                        amout_after = check_balance(symbol_call)
                        # GIÁ STOPLOSS
                        stop_price = round(price_After*0.985,6)
                        # GIÁ CHỐT LỜI 
                        sell_price = round(price_After*1.015,6)
                        create_oco_order(symbol_call,amout_after,sell_price,stop_price)
                        print("Đặt lệnh OCO thành công !")
                        break
                    else: 
                        time.sleep(1)
                # params = {'stopPrice': stop_price}
                # stop_loss_limit_order = exchange.create_order(symbol_call, 'STOP_LOSS_LIMIT', 'sell', amout_after, stop_price, params)
                # print("Lệnh stop-loss với giới hạn giá đã được tạo:", stop_loss_limit_order)
                # create_oco_order(symbol_call,amout_after,sell_price,stop_price)
            else:
                print('Số dư USDT không đủ để thực hiện giao dịch.')
        else:
            print('Cặp giao dịch không hoạt động.')
    else:
        print('Không tìm thấy cặp giao dịch trên sàn giao dịch.')
    print("--------------------------------------------------------------------------------------------------------------")


# LIMIT_COMMAND_END
#------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------
#   FUNCTION
def currentPrice(symbol):
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']
    print(f'Giá hiện tại của cặp {symbol}: {current_price}')
    return current_price

def check_balance(symbol):
    symbol_coin = symbol.split("/")[0]
    try:
        balances = exchange.fetch_balance()
        balance = balances['total'][symbol_coin]
        print("Số dư của coin: ", balance)
        return balance
    except ccxt.ExchangeError as e:
        print("Lỗi khi lấy số dư:", e)

def create_oco_order(symbol, amount, price, stop_loss_price):
    market = exchange.market(symbol)
    stop_price = stop_loss_price
    stop_limit_price = stop_loss_price

    response = exchange.private_post_order_oco({
        'symbol': market['id'],
        'side': 'SELL',  # SELL, BUY
        'quantity': exchange.amount_to_precision(symbol, amount),
        'price': exchange.price_to_precision(symbol, price),
        'stopPrice': exchange.price_to_precision(symbol, stop_price),
        'stopLimitPrice': exchange.price_to_precision(symbol, stop_limit_price),  # If provided, stopLimitTimeInForce is required
        'stopLimitTimeInForce': 'GTC',  # GTC, FOK, IOC
    })

def check_limit_buy(symbol):
    try:
        open_orders = exchange.fetch_open_orders(symbol)
        for order in open_orders:
            if order['side'] == 'buy' and order['type'] == 'limit':
                print("Lệnh mua giới hạn chưa khớp.")
                return False
        return True
    except ccxt.ExchangeError as e:
        print("Lỗi khi kiểm tra lệnh mua giới hạn:", e)

#------------------------------------------------------------------------------------------------------------------------------