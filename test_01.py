from flask import Flask, redirect, request, make_response, abort, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'username': 'wang',
        'sex': '男',
        'age': 20
    }
    return render_template('info.html', user=context)


@app.route('/user/<name>')
def wang_ge(name):
    return name


@app.route('/res')
def res():
    response = make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/love')
def love():
    return redirect('https:www.baidu.com')


@app.route('/login2', methods=['get'])
def login1():
    name = request.args.get('name')
    password = request.args.get('password')
    print(name, password)
    if name != 'wang' or password != 'admin':
        abort(404)
    return '登录成功'


@app.route('/login/<num>', endpoint='num')
def login1(num):
    if num == '1':
        context = {
            'username': 'JOHN',
            'sex': '男',
            'age': 2
        }
        return render_template('info.html', user=context)
    else:
        return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)
