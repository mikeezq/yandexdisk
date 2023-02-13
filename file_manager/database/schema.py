from sqlalchemy import MetaData
from enum import Enum, unique

from sqlalchemy import (
    Column, Date, Enum as PgEnum, ForeignKey, ForeignKeyConstraint, Integer,
    String, Table
)

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
    dir = "dir"
    file = "file"


file_system_table = Table(
    "file_system",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("parentId", Integer),
    Column("type", PgEnum(Type, name="type"), nullable=False),
    Column("url", String),
    Column("size", Integer),
    Column("data", Date, nullable=False)
)


relations_table = Table(
    "relations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("parentId", Integer),
    ForeignKeyConstraint(
        ("id", "parentId"),
        ("file_system.id", "fyle_system.parentId")
    )
)


