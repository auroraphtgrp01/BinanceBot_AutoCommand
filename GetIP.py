import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        data = response.json()
        return print(data['ip'])
    else:
        return None

# Gọi hàm để lấy địa chỉ IP công cộng
public_ip = get_public_ip()


if public_ip:
    print("Địa chỉ IP công cộng của bạn là:", public_ip)
else:
    print("Không thể lấy địa chỉ IP công cộng.")
