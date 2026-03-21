#####################################################################################
#                         API MVP QueroVisitar
#                Pós Graduação em Full Stack - PUC Rio - 2026
#                       
#                          Francisco Silveira
#
#####################################################################################

# Importa a classe OpenAPI e Info para configurar a documentação automática da API
from flask_openapi3 import OpenAPI, Info, Tag

# Importa redirect para redirecionar rotas
from flask import redirect

# Importa função para decodificar strings URL-encoded
from urllib.parse import unquote

# Importa exceção de integridade do SQLAlchemy (ex.: violação de chave única)
from sqlalchemy.exc import IntegrityError

# Importa sessão do banco e modelo Local
from model import Session, Local

# Importa logger configurado para registrar eventos
from logger import logger

# Importa schemas usados para validação e documentação
from schemas import *

# Importa CORS para permitir requisições de outros domínios
from flask_cors import CORS


# Cria informações básicas da API (nome e versão)
info = Info(title="MVP1 - API Quero Visitar", version="1.0.0")

# Inicializa a aplicação OpenAPI
app = OpenAPI(__name__, info=info)

# Habilita CORS para toda a aplicação
CORS(app)


# Define tags usadas na documentação
home_tag = Tag(name="Documentação", description="Swagger.")
local_tag = Tag(name="Locais de interesse", description="Adicionar, visualizar e remover locais de interesse para visitar")


# -----------------------------
# ROTA PRINCIPAL
# -----------------------------
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger, abrindo diretamente o ambiente para testes."""
    return redirect('/openapi/swagger')


# -----------------------------
# ADICIONAR LOCAL DE INTERESSE
# -----------------------------
@app.post('/add_local', tags=[local_tag],
          responses={"200": LocalViewSchema, "400": ErrorSchema})
def add_local(form: LocalSchema):
    """Adiciona um novo lugar de interesse à base de dados."""

    # Cria objeto Local com dados enviados no formulário
    local = Local(
        local_nome=form.local_nome,
        local_cidade=form.local_cidade,
        local_pais=form.local_pais,
        local_prioridade=form.local_prioridade
    )

    logger.debug(f"Adicionando local de interesse: '{local.local_nome}'")

    try:
        # Abre conexão com o banco
        session = Session()

        # Adiciona o lugar à sessão
        session.add(local)

        # Confirma a operação no banco
        session.commit()

        logger.debug(f"Local de Interesse adicionado: '{local.local_nome}'")

        # Retorna o local no formato definido pelo schema
        return {
            "id": local.pk_local,
            "local_nome": local.local_nome,
            "local_cidade":local.local_cidade,
            "local_pais": local.local_pais,
            "local_prioridade": local.local_prioridade
        }, 200

    except Exception as e:
        error_msg = "Não foi possível salvar o destino :/"
        logger.warning(f"Erro ao adicionar local de interesse '{local.local_nome}', {error_msg}")
        return {"message": error_msg}, 400



# ------------------------------------------------
# LISTAR OS LOCAIS DE INTERESSE POR PAIS OU TODOS
# ------------------------------------------------

@app.get('/get_lugares', tags=[local_tag],
         responses={"200": ListagemLocaisSchema, "404": ErrorSchema})
def get_lugares(query: LocalFiltroSchema):
    """Retorna todos os locais de interesse ou filtra por país."""

    session = Session()

    # Se o usuário passou ?pais=...
    if query.local_pais:
        logger.debug(f"Filtrando locais pelo país: {query.local_pais}")
        locais = session.query(Local).filter(Local.local_pais == query.local_pais).all()
    else:
        logger.debug("Coletando todos os locais de interesse")
        locais = session.query(Local).all()

    if not locais:
        return {"lugares": []}, 200

    logger.debug(f"{len(locais)} locais encontrados")
    return apresenta_locais(locais), 200



# -----------------------------------
# BUSCAR LOCAL DE INTERESSE POR NOME
# -----------------------------------
@app.get('/get_local', tags=[local_tag],
         responses={"200": LocalViewSchema, "404": ErrorSchema})
def get_local(query: LocalBuscaSchema):
    """Busca um local de interesse pelo nome."""

    nome = query.local_nome

    logger.debug(f"Coletando dados sobre local de interesse '{nome}'")

    session = Session()

    local = session.query(Local).filter(Local.local_nome == nome).first()

    if not local:
        error_msg = "Local não encontrado na base :/"
        logger.warning(f"Erro ao buscar local de interesse '{nome}', {error_msg}")
        return {"message": error_msg}, 404

    logger.debug(f"Local de interesse encontrado: '{local.local_nome}'")

    return apresenta_local(local), 200



# -------------------------------------
# DELETAR LOCAL DE INTERESSE  POR NOME
# -------------------------------------
@app.delete('/del_local', tags=[local_tag],
            responses={"200": LocalRemoveSchema, "404": ErrorSchema})
def del_lugar(query: LocalBuscaSchema):
    """Remove um local pelo nome."""

    nome = unquote(unquote(query.local_nome))

    logger.debug(f"Deletando local de interesse '{nome}'")

    session = Session()

    count = session.query(Local).filter(Local.local_nome == nome).delete()

    session.commit()

    if count:
        logger.debug(f"Local '{nome}' deletado")
        return {"message": "Local de interesse removido", "local_nome": nome}, 200

    error_msg = "Local não encontrado na base :/"
    logger.warning(f"Erro ao deletar local de interesse '{nome}', {error_msg}")
    return {"message": error_msg}, 404
