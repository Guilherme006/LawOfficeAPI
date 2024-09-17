import json
from sqlalchemy.orm import Session
from models import Cliente, Advogado, Caso, Documento
from datetime import datetime

def parse_request_body(request):
    try:
        length = int(request.headers.get('Content-Length'))
        body = request.rfile.read(length)
        return json.loads(body)
    except Exception as e:
        return {}

# --------------------
# Handlers para Cliente
# --------------------

def create_cliente(session: Session, data):
    try:
        cliente = Cliente(
            nome=data['nome'],
            email=data['email'],
            telefone=data.get('telefone'),
            endereco=data.get('endereco')  
        )
        session.add(cliente)
        session.commit()
        return {"id": cliente.id, "message": "Cliente criado com sucesso"}, 201
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400

def get_clientes(session: Session):
    clientes = session.query(Cliente).all()
    return [
        {
            "id": c.id,
            "nome": c.nome,
            "email": c.email,
            "telefone": c.telefone,
            "endereco": c.endereco  
        }
        for c in clientes
    ]

def get_cliente(session: Session, cliente_id):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        return {
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone,
            "endereco": cliente.endereco  
        }, 200
    return {"error": "Cliente não encontrado"}, 404

def update_cliente(session: Session, cliente_id, data):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        try:
            cliente.nome = data.get('nome', cliente.nome)
            cliente.email = data.get('email', cliente.email)
            cliente.telefone = data.get('telefone', cliente.telefone)
            cliente.endereco = data.get('endereco', cliente.endereco)  
            session.commit()
            return {"message": "Cliente atualizado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Cliente não encontrado"}, 404

def delete_cliente(session: Session, cliente_id):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        try:
            session.delete(cliente)
            session.commit()
            return {"message": "Cliente deletado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Cliente não encontrado"}, 404

# --------------------
# Handlers para Advogado
# --------------------

def create_advogado(session: Session, data):
    try:
        advogado = Advogado(
            nome=data['nome'],
            especialidade=data.get('especialidade'),
            telefone=data.get('telefone')  
        )
        session.add(advogado)
        session.commit()
        return {"id": advogado.id, "message": "Advogado criado com sucesso"}, 201
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400

def get_advogados(session: Session):
    advogados = session.query(Advogado).all()
    return [
        {
            "id": a.id,
            "nome": a.nome,
            "especialidade": a.especialidade,
            "telefone": a.telefone  
        }
        for a in advogados
    ]

def get_advogado(session: Session, advogado_id):
    advogado = session.query(Advogado).filter(Advogado.id == advogado_id).first()
    if advogado:
        return {
            "id": advogado.id,
            "nome": advogado.nome,
            "especialidade": advogado.especialidade,
            "telefone": advogado.telefone  
        }, 200
    return {"error": "Advogado não encontrado"}, 404

def update_advogado(session: Session, advogado_id, data):
    advogado = session.query(Advogado).filter(Advogado.id == advogado_id).first()
    if advogado:
        try:
            advogado.nome = data.get('nome', advogado.nome)
            advogado.especialidade = data.get('especialidade', advogado.especialidade)
            advogado.telefone = data.get('telefone', advogado.telefone)  
            session.commit()
            return {"message": "Advogado atualizado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Advogado não encontrado"}, 404

def delete_advogado(session: Session, advogado_id):
    advogado = session.query(Advogado).filter(Advogado.id == advogado_id).first()
    if advogado:
        try:
            session.delete(advogado)
            session.commit()
            return {"message": "Advogado deletado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Advogado não encontrado"}, 404

# --------------------
# Handlers para Caso
# --------------------

def create_caso(session: Session, data):
    try:
        # Verifica se cliente_id e advogado_id existem
        cliente = session.query(Cliente).filter(Cliente.id == data['cliente_id']).first()
        advogado = session.query(Advogado).filter(Advogado.id == data['advogado_id']).first()
        if not cliente:
            return {"error": "Cliente não encontrado"}, 404
        if not advogado:
            return {"error": "Advogado não encontrado"}, 404

        data_abertura = data.get('data_abertura')
        if data_abertura:
            data_abertura = datetime.strptime(data_abertura, "%Y-%m-%d").date()

        caso = Caso(
            descricao=data['descricao'],
            data_abertura=data_abertura,
            cliente_id=data['cliente_id'],
            advogado_id=data['advogado_id']
        )
        session.add(caso)
        session.commit()
        return {"id": caso.id, "message": "Caso criado com sucesso"}, 201
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400

def get_casos(session: Session):
    casos = session.query(Caso).all()
    return [
        {
            "id": c.id,
            "descricao": c.descricao,
            "data_abertura": c.data_abertura.isoformat() if c.data_abertura else None,
            "cliente_id": c.cliente_id,
            "advogado_id": c.advogado_id
        }
        for c in casos
    ]

def get_caso(session: Session, caso_id):
    caso = session.query(Caso).filter(Caso.id == caso_id).first()
    if caso:
        return {
            "id": caso.id,
            "descricao": caso.descricao,
            "data_abertura": caso.data_abertura.isoformat() if caso.data_abertura else None,
            "cliente_id": caso.cliente_id,
            "advogado_id": caso.advogado_id
        }, 200
    return {"error": "Caso não encontrado"}, 404

def update_caso(session: Session, caso_id, data):
    caso = session.query(Caso).filter(Caso.id == caso_id).first()
    if caso:
        try:
            caso.descricao = data.get('descricao', caso.descricao)
            data_abertura = data.get('data_abertura')
            if data_abertura:
                caso.data_abertura = datetime.strptime(data_abertura, "%Y-%m-%d").date()
            caso.cliente_id = data.get('cliente_id', caso.cliente_id)
            caso.advogado_id = data.get('advogado_id', caso.advogado_id)
            session.commit()
            return {"message": "Caso atualizado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Caso não encontrado"}, 404

def delete_caso(session: Session, caso_id):
    caso = session.query(Caso).filter(Caso.id == caso_id).first()
    if caso:
        try:
            session.delete(caso)
            session.commit()
            return {"message": "Caso deletado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Caso não encontrado"}, 404

# --------------------
# Handlers para Documento
# --------------------

def create_documento(session: Session, data):
    try:
        # Verifica se caso_id existe
        caso = session.query(Caso).filter(Caso.id == data['caso_id']).first()
        if not caso:
            return {"error": "Caso não encontrado"}, 404

        documento = Documento(
            titulo=data['titulo'],
            conteudo=data.get('conteudo'),
            caso_id=data['caso_id']
        )
        session.add(documento)
        session.commit()
        return {"id": documento.id, "message": "Documento criado com sucesso"}, 201
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400

def get_documentos(session: Session):
    documentos = session.query(Documento).all()
    return [
        {
            "id": d.id,
            "titulo": d.titulo,
            "conteudo": d.conteudo,
            "caso_id": d.caso_id
        }
        for d in documentos
    ]

def get_documento(session: Session, documento_id):
    documento = session.query(Documento).filter(Documento.id == documento_id).first()
    if documento:
        return {
            "id": documento.id,
            "titulo": documento.titulo,
            "conteudo": documento.conteudo,
            "caso_id": documento.caso_id
        }, 200
    return {"error": "Documento não encontrado"}, 404

def update_documento(session: Session, documento_id, data):
    documento = session.query(Documento).filter(Documento.id == documento_id).first()
    if documento:
        try:
            documento.titulo = data.get('titulo', documento.titulo)
            documento.conteudo = data.get('conteudo', documento.conteudo)
            documento.caso_id = data.get('caso_id', documento.caso_id)
            session.commit()
            return {"message": "Documento atualizado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Documento não encontrado"}, 404

def delete_documento(session: Session, documento_id):
    documento = session.query(Documento).filter(Documento.id == documento_id).first()
    if documento:
        try:
            session.delete(documento)
            session.commit()
            return {"message": "Documento deletado com sucesso"}, 200
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 400
    return {"error": "Documento não encontrado"}, 404
