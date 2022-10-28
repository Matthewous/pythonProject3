from turtle import title
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json

Base = declarative_base()

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'{[self.id,self.name]}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)

    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'{[self.id,self.id_book,self.id_shop,self.count]}'

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    def __str__(self):
        return f'{[self.id,self.title,self.id_publisher]}'

    stock = relationship(Stock, backref="book")


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'{[self.id,self.name]}'

    book = relationship(Book, backref="publisher")

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DATE)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def find_publisher(engine, session, pub_id=None, pub_name=None):

    if id is None:
        for p in session.query(Publisher).filter(Publisher.name == pub_name).all():
            pub_id = p[0]

    for s in session.query(Shop).join(Stock.shop).join(Book.stock).join(Publisher.book).filter(Publisher.id == pub_id):
        print(s)

def insert(engine):
       with open('/Users/matthew/Desktop/pythonProject3/SQL/Python и БД ORM/tests_data.json', 'r') as fd:
            data = json.load(fd)

            for record in data:
                model = {
                    'publisher': Publisher,
                    'shop': Shop,
                    'book': Book,
                    'stock': Stock,
                    'sale': Sale,
                }[record.get('model')]
                session.add(model(id=record.get('pk'), **record.get('fields')))

if __name__ == '__main__':

    DSN = 'postgresql://matthew:management@localhost:5432/netology_hw_1'
    engine = sqlalchemy.create_engine(DSN)
    
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    insert(engine)
    find_publisher(engine,1,None)

    session.commit()
    session.close()