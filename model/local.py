from sqlalchemy import Column, Integer, String
from model.base import Base


class Local(Base):
    __tablename__ = "Locais"

    pk_local = Column(Integer, primary_key=True, autoincrement=True)
    local_nome = Column(String(140), nullable=False)
    local_cidade = Column(String(140), nullable =False)
    local_pais = Column(String(140), nullable=False)
    local_prioridade = Column(Integer, nullable=False)