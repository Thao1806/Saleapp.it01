from saleapp.app.Models import Categories, Product


def get_categories():
    return Categories.query.all()


def get_products(kw):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()