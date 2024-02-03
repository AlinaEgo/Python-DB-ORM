import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), nullable=False)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), nullable=False)


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=80), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id', ondelete='CASCADE'))

    publishers = relationship('Publisher', cascade='all,delete', backref='book')


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id', ondelete='CASCADE'))
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id', ondelete='CASCADE'))
    count = sq.Column(sq.Integer)

    books_stock = relationship(Book, cascade='all,delete', backref='stocks')
    shops_stock = relationship(Shop, cascade='all,delete', backref='stocks')


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric(10, 2))
    date_sale = sq.Column(sq.DATE)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id', ondelete='CASCADE'))

    stock = relationship(Stock, cascade='all,delete', backref='sales')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)