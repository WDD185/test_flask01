from flask import Flask, redirect, request, make_response, abort, render_template

app = Flask(__name__)


@app.route('/')
def book():
    context = [
        {
            'name': '三国演义',
            'author': '罗贯中',
            'price': 120
        },
        {
            'name': '西游记',
            'author': '吴承恩',
            'price': 100
        },
        {
            'name': '红楼梦',
            'author': '曹雪芹',
            'price': 90
        }]

    return render_template('books.html', books=context)


if __name__ == '__main__':
    app.run(debug=True)
