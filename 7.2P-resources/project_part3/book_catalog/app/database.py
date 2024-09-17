from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://zain722_user:Ul4AlhKBwlhoUwFIlj5fsXhNV0AzFGzL@dpg-crkf948gph6c73c9990g-a.oregon-postgres.render.com/zain722" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
