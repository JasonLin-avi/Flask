from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def test():
    dic = {'name': 'hello world'}
    dic['sex'] = 'mail'
    return dic

if __name__ == '__main__':
    app.run(debug=True)
