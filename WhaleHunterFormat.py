import re


def checkNotificationFormat(message_text):
    if (message_text.upper().find('BIG WHALES') != -1 and message_text.upper().find('BINANCE') != -1 and message_text.upper().find('DURATION') != -1):
        return True
    else:
        return False


def checkSymbolToken(message_text):
    tokenCoin = ''
    Token = ''
    for char in message_text:
        if (char == '\n'):
            break
        else:
            tokenCoin += char
    if (tokenCoin.upper().find('USDT') != -1 and checkNotificationFormat(message_text)):
        Token = re.search(r'(\w+)', tokenCoin).group()
        return Token+'/USDT'
    return False


def findVolToken(message_text):
    start_index = message_text.find("24h Vol: ")
    end_index = message_text.find("K USDT", start_index)

    if start_index != -1 and end_index != -1:
        vol_value = message_text[start_index+1 + len("24h Vol: "):end_index]
        print("24h Vol:", vol_value)
    else:
        print("Không tìm thấy giá trị 24h Vol trong văn bản.")
