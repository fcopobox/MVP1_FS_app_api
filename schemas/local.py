from pydantic import BaseModel
from typing import List
from model.local import Local


class LocalSchema(BaseModel):
    """ Como um novo lugar deve ser representado: """
    local_nome: str
    local_cidade: str
    local_pais: str
    local_prioridade: int


class LocalBuscaSchema(BaseModel):
    """ Estrutura para buscar um lugar pelo nome: """
    local_nome: str


class LocalViewSchema(BaseModel):
    """ Como um lugar será retornado: """
    id: int
    local_nome: str
    local_cidade: str
    local_pais: str
    local_prioridade: int


class ListagemLocaisSchema(BaseModel):
    """ Lista de locais de interesse retornada: """
    locais: List[LocalViewSchema]


class LocalFiltroSchema(BaseModel):
    """ Lista de locais de interesse filtrada por país: """
    local_pais: str | None = None


class LocalRemoveSchema(BaseModel): 
    """ Estrutura de retorno ao deletar: """
    message: str
    local_nome: str


def apresenta_local(local: Local):
    """ Retorna um local de interesse no formato esperado. """
    return {
        "id": local.pk_local,
        "local_nome": local.local_nome,
        "local_cidade": local.local_cidade,
        "local_pais": local.local_pais,
        "local_prioridade": local.local_prioridade
    }


def apresenta_locais(locais: List[Local]):
    """ Retorna uma lista de locais de interesse no formato esperado. """
    return {
        "locais": [apresenta_local(l) for l in locais]
    }

