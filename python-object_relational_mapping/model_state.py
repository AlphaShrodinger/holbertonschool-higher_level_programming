#!/usr/bin/python3
'''contains the class definition of a State and an instance'''


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = 'mysql://username:password@localhost:3306/database_name'
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    from state import State
    Base.metadata.create_all(engine)

    session = Session()
    new_state = State(name='New State')
    session.add(new_state)
    session.commit()
    session.close()
