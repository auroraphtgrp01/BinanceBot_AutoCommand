from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/start", methods=['POST'])
def start_function():
    # Kiểm tra xem button có tên 'startButton' đã được nhấn hay chưa
    if request.method == "POST":
        
        # Gọi hàm Python mà bạn muốn khởi động tại đây
        # Ví dụ: my_function()
        
        return render_template('index.html')

    



if __name__ == '__main__':
    app.run()
