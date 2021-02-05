from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from helpers.Parser import parsing

engine = create_engine('sqlite:///testwork.db', echo=True)
base = declarative_base()
session = sessionmaker(bind=engine)()


class Log(base):
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


def main():
    base.metadata.create_all(engine)
    session.commit()
    with open('logs.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        info_dict = parsing(line)

        dt = datetime.strptime(info_dict['date'], "%Y-%m-%d %H:%M:%S")

        db_log = Log(id_strind=info_dict["id_string"],
                     IP=info_dict['IP'],
                     link=info_dict["link"],
                     created_at=dt)
        session.add(db_log)
    session.commit()


if __name__ == '__main__':
    main()

