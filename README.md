Desafio Backend, uma aplicação web que permite o enviou de um arquivo CNAB. Os dados do arquivo são armazenados em um banco de dados relacional, e disponibilizados para consulta.

## Instruções

Como instalar esse projeto:

- Faça um clone deste repositório;
- Na raiz do projeto clonado, crie um ambiante virtual, rode o comando `python -m venv venv`;
- Ative o a ambiante virtual, rode o comando `source venv/bin/activate`;
- Instale as dependencias do projeto, rode o comando `pip install -r requirements.txt`;
- Execute a migrations, rode o comando `python manage.py migrate`;
- Execute a fixture transactionTypes.json para prencher a tabela de transaction_types, rode o comando `python manage.py loaddata transactionTypes.json`;
- Finalmente rode o comando `python manage.py runserver`;
- No seu navegador, acesse http://127.0.0.1:8000/api/upload/.
- Envie um arquivo txt com seu CNAB
