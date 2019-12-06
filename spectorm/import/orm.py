from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey, UniqueConstraint, TIMESTAMP, \
    Float, Date, Boolean

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, relationship


def model_factory(dic, Base):
    """This function creates custom ORM classes from the user config"""
    new_dic = {}
    name = dic["name"]
    new_dic["__tablename__"] = name

    new_dic["id"] = Column(Integer, primary_key=True)
    new_dic["timestamp"] = Column(TIMESTAMP)

    for column in dic["columns"]:
        new_dic[column] = Column(Text)

    return type(name, (Base,), new_dic)


def run_test():
    """for test purpose only"""
    speclist = read_spec_config("spec_conf.json")
    engine = create_engine('sqlite:///orm.db', echo=True)
    Base = declarative_base()
    orm_classes = [model_factory(i, Base) for i in speclist]
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()