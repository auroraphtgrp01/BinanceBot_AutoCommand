import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        data = response.json()
        return print(data['ip'])
    else:
        return None

# Gọi hàm để lấy địa chỉ IP công cộng
get_public_ip()

