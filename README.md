## TDE01 - Arquitetura de Banco de Dados

Esse projeto se trata de um trabalho para a disciplina de arquitetura de banco de dados do curso de Ciência da Computação. 

Este projeto apresenta a **LawOfficeAPI**, uma API RESTful desenvolvida para gerenciar as operações de um escritório de advocacia. A API foi construída utilizando Python como linguagem de programação, SQLAlchemy para mapeamento objeto-relacional (ORM) e SQLite como sistema de gerenciamento de banco de dados. 

O projeto abrange a criação, leitura, atualização e deleção (CRUD) de entidades fundamentais como Clientes, Advogados, Casos e Documentos. Além disso, testes automatizados foram implementados utilizando **pytest** e **requests** para garantir a robustez e a confiabilidade das funcionalidades desenvolvidas. 

### Construido com

![visual-studio-code]
![python]
![SQLite Badge]
![SQLAlchemy Badge]
![Pytest Badge]

### Ferramentas

- **Uuid:** Gera identificadores únicos para garantir que cada e-mail e nome sejam únicos, evitando conflitos de unicidade.
- **SQLAlchemy:** Para mapeamento objeto-relacional e interação com o banco de dados.
- **Pytest:** Para a execução de testes automatizados.
- **Requests:** Para realizar requisições HTTP durante os testes.

### Configuração

Para configurar e executar a LawOfficeAPI, siga os passos abaixo:

1. Clone o repositório do projeto para sua máquina local:

   ```sh
   git clone https://github.com/Guilherme006/LawOfficeAPI.git
   ```

2. Instale as dependências:

   ```sh
   pip install -r requeriments.txt
   ```

3. Execute o servidor e aproveite os testes.


<!-- Badges -->
[visual-studio-code]: https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=for-the-badge
[python]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge
[SQLite Badge]: https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=for-the-badge
[SQLAlchemy Badge]: https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=fff&style=flat-square
[Pytest Badge]: https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=fff&style=flat-square
