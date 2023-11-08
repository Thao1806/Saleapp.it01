from flask import render_template, request
import dao
from saleapp.app import app


@app.route('/')
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    products = dao.get_products(kw)
    return render_template('index.html', categories=cates, products=products)


if __name__ == '__main__':
    from saleapp.app import admin
    app.run(debug=True)