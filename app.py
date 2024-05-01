from flask import Flask, make_response
from flask import request
from logging import Logger

app = Flask(__name__)

@app.route('/')
def hello():
    # 取得特定 header 的值
    header_value = request.headers.get('x-jwt')
    print(header_value)
    if header_value != 'Jason':
        app.logger.warning('not accept token')
        return make_response('Hello, world! 123',403)
    
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
