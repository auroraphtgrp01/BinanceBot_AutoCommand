from flask import Flask, request
from flask import Flask, render_template
import requests
import GetIP
app = Flask(__name__, template_folder='E:/Python/templates/')


@app.route("/")
def main():
    return render_template('E:/Python/templates/index.html')


@app.route("/start", methods=['POST'])
def start_function():
    # Kiểm tra xem button có tên 'startButton' đã được nhấn hay chưa
    if request.method == "POST":
        
        # Gọi hàm Python mà bạn muốn khởi động tại đây
        # Ví dụ: my_function()
        
        return render_template('E:/Python/templates/index.html')
    
   

if __name__ == "__main__":
    app.run(debug=True, port=8001)
