# DW-2910
## Para experimentar os exemplos deste projeto lembre-se de:

1. dentro do projeto backend criar os diretórios:
- instance
    - uploads
    - settings.toml

> Para execução local, o conteúdo de settins será:

`
[default]
SECRET_KEY = "123456"
EXTENSIONS = [ "backend.ext.database:init_app", "backend.ext.cors:init_app", "backend.blueprints.upload.upload:init_app", "backend.blueprints.api_v1.api_v1:init_app",]
SQLALCHEMY_DATABASE_URI = "sqlite:{{CAMINHO PARA SEU REPOSITÓRIO LOCAL}}/dw-2910/backend/instance/db.sqlite3"
SQLALCHEMY_TRACK_MODIFICATIONS = false
`

2. Crie um virtualenv com ferramenta de sua preferência (poetry, pyenv...) e instale os requirements

3. Garanta que o banco será criado e as entidades criadas, no diretório raiz do backend, execute:
`$ python manage.py db-upgrade`

4. Execute o servidor do backend:
`$ python manage.py runserver`

5. Abra um segundo terminal e vá até o diretório do frontend para executar o serviço
`$ npm run serve`

6. Acesse a URL do frontend conforme aparece no terminal.