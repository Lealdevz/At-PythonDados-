from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Movie, Series

Base = declarative_base()

class MovieBase(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    year = Column(Integer)
    rating = Column(Float)

class SeriesBase(Base):
    __tablename__ = 'series'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    year = Column(Integer)
    seasons = Column(Integer)
    episodes = Column(Integer)

def salvar_banco(catalog, db_nome):
    engine = create_engine(f'sqlite:///{db_nome}', echo=False)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in catalog:
        objeto = None
        if isinstance(item, Movie):
            objeto = MovieBase(title=item.title, year=item.year, rating=item.rating) 
        elif isinstance(item, Series):
            objeto = SeriesBase(title=item.title, year=item.year, seasons=item.seasons, episodes=item.episodes) 

        if objeto:
            try:
                session.add(objeto)
                session.commit()
            except IntegrityError:
                session.rollback()
                print(f"Item '{objeto.title}' já existe no banco de dados.")
            except Exception as e:
                session.rollback()
                print(e)       
    return engine