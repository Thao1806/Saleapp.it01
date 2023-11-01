from saleapp.app import db, app
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship
class Categories(db.Model):
    __tablename__='categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name= Column(String(50), nullable=False, unique= True)
    Product= relationship('Product',backref='Categories', lazy=True)
class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name= Column(String(50), nullable=False, unique= True)
    price= Column(Float, default=0)
    image= Column(String(100))
    categories_id= Column(Integer, ForeignKey(Categories.id),nullable=False)
if __name__=='__main__':
    with app.app_context():
        # c1= Categories(name='Mobile')
        # c2= Categories(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        db.create_all()