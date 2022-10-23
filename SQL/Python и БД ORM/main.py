import sqlalchemy
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://matthew:management@localhost:5432/netology_hw_1'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)

session = Session()







session.close()