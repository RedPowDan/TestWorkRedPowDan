from datetime import datetime
from db.database import db_session
from helpers import parsing
from db.database import init_db
from db.models import Log


start_main = True


def main():
    with open('logs.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        info_dict = parsing(line)

        dt = datetime.strptime(info_dict['date'], "%Y-%m-%d %H:%M:%S")

        db_log = Log(id_strind=info_dict["id_string"],
                     IP=info_dict['IP'],
                     link=info_dict["link"],
                     created_at=dt)
        db_session.add(db_log)
    db_session.commit()


if start_main:
    main()
