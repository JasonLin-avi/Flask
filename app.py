from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response('Hello, world! 123')
    response.set_cookie('token','token value')
    
    return response

@app.route('/test')
def test():
    dic = {'name': 'hello world'}
    dic['sex'] = 'mail'
    return dic

if __name__ == '__main__':
    app.run(debug=True)
