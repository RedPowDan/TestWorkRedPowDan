from sqlalchemy import Column, VARCHAR, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base

from db.database import Base


class Log(Base):
    __tablename__ = 'logs'

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    id_string = Column(VARCHAR(8), nullable=False, unique=True)
    IP = Column(VARCHAR(15), nullable=False)
    link = Column(VARCHAR(200))

    created_at = Column(
        TIMESTAMP,
        nullable=False,
    )

    def __init__(self, id_strind, IP, link, created_at):
        self.id_string = id_strind
        self.IP = IP
        self.link = link
        self.created_at = created_at
