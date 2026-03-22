#####################################################################################
#                         API MVP QueroVisitar
#                Pós Graduação em Full Stack - PUC Rio - 2026
#                       
#                          Francisco Silveira
#
####################################################################################


Este projeto é o Back-End para o MVP da Disciplina **Desenvolvimento Full Stack Básico** 

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais. Você pode criar um ambiente virtual executando o comando abaixo (ou utilizar outro ambiente virtual a sua escolha) 
-----------------------------------
Python3 -m venv env
-----------------------------------

> Para ativar o ambiente virtual execute
-----------------------------------
.\env\Scripts\activate.ps1
-----------------------------------

Ao ativar o ambiente virtual o prompt do terminal passará a ter o prefixo '(env)'

> Para instalar as bibliotecas necessárias, execute a partir do diretório principal
-----------------------------------
pip install -r requirements.txt
-----------------------------------

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

> Para executar a API basta executar:
-----------------------------------
flask run --host 0.0.0.0 --port 5000
-----------------------------------


Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após salvar uma mudança no código fonte. 
-----------------------------------
flask run --host 0.0.0.0 --port 5000 --reload
-----------------------------------

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Para parar a execução, no Terminal digite CTRL+c

Para desativar o ambiente virtual execute 
-----------------------------------
deactivate 
-----------------------------------

caso deseje remover completamente o ambiente virtual do projeto, execute em seguida  
-----------------------------------
Remove-Item -Recurse -Force env
-----------------------------------
