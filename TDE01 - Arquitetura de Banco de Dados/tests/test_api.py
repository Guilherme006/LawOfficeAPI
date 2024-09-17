import pytest
import requests
import uuid

BASE_URL = "http://localhost:8000"

@pytest.fixture(scope="function")
def cliente_data():
    unique_id = uuid.uuid4()
    return {
        "nome": f"Teste Cliente {unique_id}",
        "email": f"cliente.teste.{unique_id}@example.com",
        "telefone": "9999-9999",
        "endereco": "Rua Teste, 123"
    }

@pytest.fixture(scope="function")
def advogado_data():
    unique_id = uuid.uuid4()
    return {
        "nome": f"Teste Advogado {unique_id}",
        "especialidade": "Direito Trabalhista",
        "telefone": "8888-8888"
    }

@pytest.fixture(scope="function")
def documento_data():
    unique_id = uuid.uuid4()
    return {
        "titulo": f"Documento de Teste {unique_id}",
        "conteudo": "Conteúdo do documento de teste."
    }

def test_criar_cliente(cliente_data):
    response = requests.post(f"{BASE_URL}/clientes", json=cliente_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["message"] == "Cliente criado com sucesso"
    return data["id"]

def test_obter_clientes():
    response = requests.get(f"{BASE_URL}/clientes")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obter_cliente_especifico():
    # Primeiro, criar um cliente para obter o ID
    cliente = {
        "nome": "Cliente Específico",
        "email": "especifico@example.com",
        "telefone": "7777-7777",
        "endereco": "Avenida Específico, 456"
    }
    post_response = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_response.status_code == 201
    cliente_id = post_response.json()["id"]

    # Agora, obter o cliente específico
    get_response = requests.get(f"{BASE_URL}/clientes/{cliente_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == cliente_id
    assert data["nome"] == cliente["nome"]
    assert data["email"] == cliente["email"]
    assert data["telefone"] == cliente["telefone"]
    assert data["endereco"] == cliente["endereco"]

    # Limpar: deletar o cliente criado
    delete_response = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_response.status_code == 200

def test_atualizar_cliente():
    # Criar um cliente
    cliente = {
        "nome": "Cliente Atualizar",
        "email": "atualizar@example.com",
        "telefone": "6666-6666",
        "endereco": "Rua Atualizar, 789"
    }
    post_response = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_response.status_code == 201
    cliente_id = post_response.json()["id"]

    # Atualizar o cliente
    atualizacao = {
        "telefone": "5555-5555",
        "endereco": "Rua Atualizada, 101"
    }
    put_response = requests.put(f"{BASE_URL}/clientes/{cliente_id}", json=atualizacao)
    assert put_response.status_code == 200
    assert put_response.json()["message"] == "Cliente atualizado com sucesso"

    # Verificar as atualizações
    get_response = requests.get(f"{BASE_URL}/clientes/{cliente_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["telefone"] == atualizacao["telefone"]
    assert data["endereco"] == atualizacao["endereco"]

    # Limpar: deletar o cliente
    delete_response = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_response.status_code == 200

def test_deletar_cliente():
    # Criar um cliente
    cliente = {
        "nome": "Cliente Deletar",
        "email": "deletar@example.com",
        "telefone": "4444-4444",
        "endereco": "Avenida Deletar, 202"
    }
    post_response = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_response.status_code == 201
    cliente_id = post_response.json()["id"]

    # Deletar o cliente
    delete_response = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Cliente deletado com sucesso"

    # Verificar se o cliente foi deletado
    get_response = requests.get(f"{BASE_URL}/clientes/{cliente_id}")
    assert get_response.status_code == 404
    assert get_response.json()["error"] == "Cliente não encontrado"

# ===========================
# Testes para Advogado
# ===========================

def test_criar_advogado(advogado_data):
    response = requests.post(f"{BASE_URL}/advogados", json=advogado_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["message"] == "Advogado criado com sucesso"
    return data["id"]

def test_obter_advogados():
    response = requests.get(f"{BASE_URL}/advogados")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obter_advogado_especifico():
    # Primeiro, criar um advogado para obter o ID
    advogado = {
        "nome": "Advogado Específico",
        "especialidade": "Direito Tributário",
        "telefone": "3333-3333"
    }
    post_response = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_response.status_code == 201
    advogado_id = post_response.json()["id"]

    # Agora, obter o advogado específico
    get_response = requests.get(f"{BASE_URL}/advogados/{advogado_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == advogado_id
    assert data["nome"] == advogado["nome"]
    assert data["especialidade"] == advogado["especialidade"]
    assert data["telefone"] == advogado["telefone"]

    # Limpar: deletar o advogado criado
    delete_response = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_response.status_code == 200

def test_atualizar_advogado():
    # Criar um advogado
    advogado = {
        "nome": "Advogado Atualizar",
        "especialidade": "Direito Ambiental",
        "telefone": "2222-2222"
    }
    post_response = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_response.status_code == 201
    advogado_id = post_response.json()["id"]

    # Atualizar o advogado
    atualizacao = {
        "especialidade": "Direito Civil",
        "telefone": "1111-1111"
    }
    put_response = requests.put(f"{BASE_URL}/advogados/{advogado_id}", json=atualizacao)
    assert put_response.status_code == 200
    assert put_response.json()["message"] == "Advogado atualizado com sucesso"

    # Verificar as atualizações
    get_response = requests.get(f"{BASE_URL}/advogados/{advogado_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["especialidade"] == atualizacao["especialidade"]
    assert data["telefone"] == atualizacao["telefone"]

    # Limpar: deletar o advogado
    delete_response = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_response.status_code == 200

def test_deletar_advogado():
    # Criar um advogado
    advogado = {
        "nome": "Advogado Deletar",
        "especialidade": "Direito Internacional",
        "telefone": "0000-0000"
    }
    post_response = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_response.status_code == 201
    advogado_id = post_response.json()["id"]

    # Deletar o advogado
    delete_response = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Advogado deletado com sucesso"

    # Verificar se o advogado foi deletado
    get_response = requests.get(f"{BASE_URL}/advogados/{advogado_id}")
    assert get_response.status_code == 404
    assert get_response.json()["error"] == "Advogado não encontrado"

# ===========================
# Testes para Caso
# ===========================

def test_criar_caso(cliente_data, advogado_data):
    # Primeiro, criar um cliente
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente_data)
    assert post_cliente.status_code == 201, f"Erro ao criar cliente: {post_cliente.text}"
    cliente_id = post_cliente.json()["id"]

    # Criar um advogado
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado_data)
    assert post_advogado.status_code == 201, f"Erro ao criar advogado: {post_advogado.text}"
    advogado_id = post_advogado.json()["id"]

    # Criar um caso
    caso = {
        "descricao": "Processo de Teste Automatizado",
        "data_abertura": "2024-02-02",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_response = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_response.status_code == 201, f"Erro ao criar caso: {post_response.text}"
    caso_id = post_response.json()["id"]

    # Limpar: deletar o caso, advogado e cliente
    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200, f"Erro ao deletar caso: {delete_caso.text}"

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200, f"Erro ao deletar advogado: {delete_advogado.text}"

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200, f"Erro ao deletar cliente: {delete_cliente.text}"


def test_obter_casos():
    response = requests.get(f"{BASE_URL}/casos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obter_caso_especifico():
    # Criar um cliente e advogado
    cliente = {
        "nome": "Cliente para Caso Específico",
        "email": "caso.especifico@example.com",
        "telefone": "1234-5678",
        "endereco": "Rua Caso Específico, 321"
    }
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_cliente.status_code == 201
    cliente_id = post_cliente.json()["id"]

    advogado = {
        "nome": "Advogado para Caso Específico",
        "especialidade": "Direito de Família",
        "telefone": "8765-4321"
    }
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_advogado.status_code == 201
    advogado_id = post_advogado.json()["id"]

    # Criar um caso
    caso = {
        "descricao": "Processo de Divórcio Específico",
        "data_abertura": "2024-03-03",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201
    caso_id = post_caso.json()["id"]

    # Obter o caso específico
    get_response = requests.get(f"{BASE_URL}/casos/{caso_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == caso_id
    assert data["descricao"] == caso["descricao"]
    assert data["data_abertura"] == caso["data_abertura"]
    assert data["cliente_id"] == cliente_id
    assert data["advogado_id"] == advogado_id

    # Limpar: deletar o caso, advogado e cliente
    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200

def test_atualizar_caso():
    # Criar um cliente e advogado
    cliente = {
        "nome": "Cliente para Atualizar Caso",
        "email": "atualizar.caso@example.com",
        "telefone": "2222-2222",
        "endereco": "Rua Atualizar Caso, 654"
    }
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_cliente.status_code == 201
    cliente_id = post_cliente.json()["id"]

    advogado = {
        "nome": "Advogado para Atualizar Caso",
        "especialidade": "Direito Penal",
        "telefone": "3333-3333"
    }
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_advogado.status_code == 201
    advogado_id = post_advogado.json()["id"]

    # Criar um caso
    caso = {
        "descricao": "Processo Penal Inicial",
        "data_abertura": "2024-04-04",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201
    caso_id = post_caso.json()["id"]

    # Atualizar o caso
    atualizacao = {
        "descricao": "Processo Penal Atualizado",
        "data_abertura": "2024-05-05"
    }
    put_response = requests.put(f"{BASE_URL}/casos/{caso_id}", json=atualizacao)
    assert put_response.status_code == 200
    assert put_response.json()["message"] == "Caso atualizado com sucesso"

    # Verificar as atualizações
    get_response = requests.get(f"{BASE_URL}/casos/{caso_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["descricao"] == atualizacao["descricao"]
    assert data["data_abertura"] == atualizacao["data_abertura"]

    # Limpar: deletar o caso, advogado e cliente
    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200

def test_deletar_caso():
    # Criar um cliente e advogado
    cliente = {
        "nome": "Cliente para Deletar Caso",
        "email": "deletar.caso@example.com",
        "telefone": "4444-4444",
        "endereco": "Avenida Deletar Caso, 987"
    }
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_cliente.status_code == 201
    cliente_id = post_cliente.json()["id"]

    advogado = {
        "nome": "Advogado para Deletar Caso",
        "especialidade": "Direito Empresarial",
        "telefone": "5555-5555"
    }
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_advogado.status_code == 201
    advogado_id = post_advogado.json()["id"]

    # Criar um caso
    caso = {
        "descricao": "Processo Empresarial",
        "data_abertura": "2024-06-06",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201
    caso_id = post_caso.json()["id"]

    # Deletar o caso
    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200
    assert delete_caso.json()["message"] == "Caso deletado com sucesso"

    # Verificar se o caso foi deletado
    get_response = requests.get(f"{BASE_URL}/casos/{caso_id}")
    assert get_response.status_code == 404
    assert get_response.json()["error"] == "Caso não encontrado"

    # Limpar: deletar o advogado e cliente
    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200

# ===========================
# Testes para Documento
# ===========================

def test_criar_documento(cliente_data, advogado_data, documento_data):
    # Criar um cliente
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente_data)
    assert post_cliente.status_code == 201, f"Erro ao criar cliente: {post_cliente.text}"
    cliente_id = post_cliente.json()["id"]

    # Criar um advogado
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado_data)
    assert post_advogado.status_code == 201, f"Erro ao criar advogado: {post_advogado.text}"
    advogado_id = post_advogado.json()["id"]

    # Criar um caso
    caso = {
        "descricao": "Processo para Documento",
        "data_abertura": "2024-07-07",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201, f"Erro ao criar caso: {post_caso.text}"
    caso_id = post_caso.json()["id"]

    # Criar um documento
    documento = {
        "titulo": documento_data["titulo"],
        "conteudo": documento_data["conteudo"],
        "caso_id": caso_id
    }
    post_documento = requests.post(f"{BASE_URL}/documentos", json=documento)
    assert post_documento.status_code == 201, f"Erro ao criar documento: {post_documento.text}"
    documento_id = post_documento.json()["id"]

    # Limpar: deletar o documento, caso, advogado e cliente
    delete_documento = requests.delete(f"{BASE_URL}/documentos/{documento_id}")
    assert delete_documento.status_code == 200, f"Erro ao deletar documento: {delete_documento.text}"

    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200, f"Erro ao deletar caso: {delete_caso.text}"

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200, f"Erro ao deletar advogado: {delete_advogado.text}"

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200, f"Erro ao deletar cliente: {delete_cliente.text}"


def test_obter_documentos():
    response = requests.get(f"{BASE_URL}/documentos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obter_documento_especifico():
    # Criar um cliente e advogado
    cliente = {
        "nome": "Cliente para Documento Específico",
        "email": "doc.especifico@example.com",
        "telefone": "6666-6666",
        "endereco": "Rua Documento Específico, 654"
    }
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_cliente.status_code == 201
    cliente_id = post_cliente.json()["id"]

    advogado = {
        "nome": "Advogado para Documento Específico",
        "especialidade": "Direito Contratual",
        "telefone": "7777-7777"
    }
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_advogado.status_code == 201
    advogado_id = post_advogado.json()["id"]

    # Criar um caso
    caso = {
        "descricao": "Processo para Documento Específico",
        "data_abertura": "2024-08-08",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201
    caso_id = post_caso.json()["id"]

    # Criar um documento
    documento = {
        "titulo": "Documento Específico",
        "conteudo": "Conteúdo específico do documento.",
        "caso_id": caso_id
    }
    post_documento = requests.post(f"{BASE_URL}/documentos", json=documento)
    assert post_documento.status_code == 201
    documento_id = post_documento.json()["id"]

    # Obter o documento específico
    get_response = requests.get(f"{BASE_URL}/documentos/{documento_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == documento_id
    assert data["titulo"] == documento["titulo"]
    assert data["conteudo"] == documento["conteudo"]
    assert data["caso_id"] == caso_id

    # Limpar: deletar o documento, caso, advogado e cliente
    delete_documento = requests.delete(f"{BASE_URL}/documentos/{documento_id}")
    assert delete_documento.status_code == 200

    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200

def test_atualizar_documento():
    # Criar um cliente, advogado e caso
    cliente = {
        "nome": "Cliente para Atualizar Documento",
        "email": "atualizar.doc@example.com",
        "telefone": "8888-8888",
        "endereco": "Avenida Atualizar Documento, 321"
    }
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_cliente.status_code == 201
    cliente_id = post_cliente.json()["id"]

    advogado = {
        "nome": "Advogado para Atualizar Documento",
        "especialidade": "Direito Societário",
        "telefone": "9999-9999"
    }
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_advogado.status_code == 201
    advogado_id = post_advogado.json()["id"]

    caso = {
        "descricao": "Processo para Atualizar Documento",
        "data_abertura": "2024-09-09",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201
    caso_id = post_caso.json()["id"]

    # Criar um documento
    documento = {
        "titulo": "Documento para Atualizar",
        "conteudo": "Conteúdo original do documento.",
        "caso_id": caso_id
    }
    post_documento = requests.post(f"{BASE_URL}/documentos", json=documento)
    assert post_documento.status_code == 201
    documento_id = post_documento.json()["id"]

    # Atualizar o documento
    atualizacao = {
        "titulo": "Documento Atualizado",
        "conteudo": "Conteúdo atualizado do documento."
    }
    put_response = requests.put(f"{BASE_URL}/documentos/{documento_id}", json=atualizacao)
    assert put_response.status_code == 200
    assert put_response.json()["message"] == "Documento atualizado com sucesso"

    # Verificar as atualizações
    get_response = requests.get(f"{BASE_URL}/documentos/{documento_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["titulo"] == atualizacao["titulo"]
    assert data["conteudo"] == atualizacao["conteudo"]

    # Limpar: deletar o documento, caso, advogado e cliente
    delete_documento = requests.delete(f"{BASE_URL}/documentos/{documento_id}")
    assert delete_documento.status_code == 200

    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200

def test_deletar_documento():
    # Criar um cliente, advogado e caso
    cliente = {
        "nome": "Cliente para Deletar Documento",
        "email": "deletar.doc@example.com",
        "telefone": "0000-0000",
        "endereco": "Rua Deletar Documento, 654"
    }
    post_cliente = requests.post(f"{BASE_URL}/clientes", json=cliente)
    assert post_cliente.status_code == 201
    cliente_id = post_cliente.json()["id"]

    advogado = {
        "nome": "Advogado para Deletar Documento",
        "especialidade": "Direito Administrativo",
        "telefone": "1111-1111"
    }
    post_advogado = requests.post(f"{BASE_URL}/advogados", json=advogado)
    assert post_advogado.status_code == 201
    advogado_id = post_advogado.json()["id"]

    caso = {
        "descricao": "Processo para Deletar Documento",
        "data_abertura": "2024-10-10",
        "cliente_id": cliente_id,
        "advogado_id": advogado_id
    }
    post_caso = requests.post(f"{BASE_URL}/casos", json=caso)
    assert post_caso.status_code == 201
    caso_id = post_caso.json()["id"]

    # Criar um documento
    documento = {
        "titulo": "Documento para Deletar",
        "conteudo": "Conteúdo do documento a ser deletado.",
        "caso_id": caso_id
    }
    post_documento = requests.post(f"{BASE_URL}/documentos", json=documento)
    assert post_documento.status_code == 201
    documento_id = post_documento.json()["id"]

    # Deletar o documento
    delete_documento = requests.delete(f"{BASE_URL}/documentos/{documento_id}")
    assert delete_documento.status_code == 200
    assert delete_documento.json()["message"] == "Documento deletado com sucesso"

    # Verificar se o documento foi deletado
    get_response = requests.get(f"{BASE_URL}/documentos/{documento_id}")
    assert get_response.status_code == 404
    assert get_response.json()["error"] == "Documento não encontrado"

    # Limpar: deletar o caso, advogado e cliente
    delete_caso = requests.delete(f"{BASE_URL}/casos/{caso_id}")
    assert delete_caso.status_code == 200

    delete_advogado = requests.delete(f"{BASE_URL}/advogados/{advogado_id}")
    assert delete_advogado.status_code == 200

    delete_cliente = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
    assert delete_cliente.status_code == 200
