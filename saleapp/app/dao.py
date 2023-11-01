def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'IPhone 13',
        'prices': '2.000.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg'
    }, {
        'id': 2,
        'name': 'IPhone 100',
        'prices': '1.000.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg'
    }, {
        'id': 3,
        'name': 'Galaxy 1300',
        'prices': '2.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg'
    }, {
        'id': 4,
        'name': 'Nokia đập đá 13',
        'prices': '2.000.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg'
    }, {
        'id': 5,
        'name': 'Oppo Sơn Tùng 13',
        'prices': '12.000.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg'
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products
