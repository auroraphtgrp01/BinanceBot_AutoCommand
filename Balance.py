import ccxt

# Cài đặt thông tin API của bạn
api_key = 'IGDKTUg929EQ91wXyQ1eyc3U5jIDXoKtkdajL7Vc6CVIcriMFDP4WEpPi611lqAI'
api_secret = 'rxcpcXxM7enU9d9gWx8YuJev0xOrLXlCOenovWn6Qxd3u0T6frUPt9t3fLtJKIkP'

# Khởi tạo kết nối với sàn Binance
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret
})

# Lấy số dư ví Spot
def get_spot_balance():
    balance = exchange.fetch_balance()
    for asset, amount in balance['total'].items():
        if amount > 0:
            print(f'{asset}: {amount}')

# Gọi hàm để lấy số dư ví Spot
get_spot_balance()