from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Date, Enum as PgEnum, Integer, String

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),

    # Именование индексов
    'ix': 'ix__%(table_name)s__%(all_column_names)s',

    # Именование уникальных индексов
    'uq': 'uq__%(table_name)s__%(all_column_names)s',

    # Именование CHECK-constraint-ов
    'ck': 'ck__%(table_name)s__%(constraint_name)s',

    # Именование внешних ключей
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',

    # Именование первичных ключей
    'pk': 'pk__%(table_name)s'
}
metadata = MetaData(naming_convention=convention)


class Type(Enum):
    folder = "FOLDER"
    file = "FILE"


Base = declarative_base(metadata=metadata)


class FileSystem(Base):
    __tablename__ = "file_system"
    id = Column(Integer, primary_key=True, nullable=False)
    parentId = Column(Integer, ForeignKey("relations.id"))
    type = Column(PgEnum(Type, name="type"), nullable=False)
    url = Column(String)
    size = Column(Integer)
    data = Column(Date, nullable=False)


class Relations(Base):
    __tablename__ = "relations"
    id = Column(Integer, primary_key=True, nullable=False)
    children = relationship("FileSystem")
    type = Column(PgEnum(Type, name="type"), nullable=False)
    url = Column(String)
    size = Column(Integer)
    data = Column(Date, nullable=False)
