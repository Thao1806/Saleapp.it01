from saleapp.app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    avatar = Column(String(150),
                    default='https://vietbaiseothue.com/wp-content/uploads/2017/11/icon-nhan-vien-400x400.png')

    def __str__(self):
        return self.name


class Categories(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    Product = relationship('Product', backref='Categories', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    categories_id = Column(Integer, ForeignKey(Categories.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib

        u1 = User(name='My van', username='My Van',
                  password=str(hashlib.md5('1234567'.encode('utf-8')).hexdigest()))
        u2 = User(name='Nhat Thao', username='Nhat Thao',
                  password=str(hashlib.md5('12345678'.encode('utf-8')).hexdigest()))
        db.session.add(u1)
        db.session.add(u2)
        # c1 = Categories(name='Mobile')
        # c2 = Categories(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        # p1 = Product(name='iPhone 13', price=20000000, categories_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        # p2 = Product(name='Galaxy S23', price=21000000, categories_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        # p3 = Product(name='iPad Pro 2023', price=22000000, categories_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        # p4 = Product(name='Galaxy Tab S9', price=28000000, categories_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        # p5 = Product(name='Note 13', price=20000000, categories_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        #
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
