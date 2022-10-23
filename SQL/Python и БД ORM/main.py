from turtle import title
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(publisher, backref="books")

class shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)

    book = relationship(book, backref="stocks")
    shop = relationship(shop, backref="stocks")

class sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.DATE)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    ount = sq.Column(sq.Integer)

    stock = relationship(stock, backref="sales")


if __name__ == '__main__':

    DSN = 'postgresql://matthew:management@localhost:5432/netology_hw_1'
    engine = sqlalchemy.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()


    session.close()