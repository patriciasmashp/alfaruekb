from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine

import config


engine = create_async_engine(url=config.DB_ASYNC_DRIVER + config.DB_URL, echo=True)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

def create_sync_engine():
    engine = create_engine(url=config.DB_SYNC_DRIVER + config.DB_URL)    
    return engine