from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    input_ = request.args.get('input', default=1, type=int)
    print("Received query:", request.url)
    data = compute_heavy_function(input_)
    return render_template('index.html', fibo=data)

def compute_heavy_function(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return compute_heavy_function(n-1) + compute_heavy_function(n-2)


if __name__ == '__main__':
    app.run()
