from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

DATABASE_URI = "sqlite:///./spy_cat_agency.db"

engine = create_engine(url=DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_sync_session():
    with SessionLocal() as session:
        yield session
        session.commit()
