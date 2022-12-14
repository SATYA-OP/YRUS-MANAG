from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from AaruRobot import DB_URI
from AaruRobot import LOGGER as log

if DB_URI and DB_URI.startswith("postgres://lqbjsmtk:WGRHF4-POZI7gaVuACCSPSSMvB2HGt4O@tiny.db.elephantsql.com/lqbjsmtk"):
    DB_URI = DB_URI.replace("postgres://lqbjsmtk:WGRHF4-POZI7gaVuACCSPSSMvB2HGt4O@tiny.db.elephantsql.com/lqbjsmtk", "postgresql://", 1)


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    log.info("[PostgreSQL] Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
