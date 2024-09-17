from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String)
    endereco = Column(String)  
    
    casos = relationship('Caso', back_populates='cliente', cascade="all, delete-orphan")

class Advogado(Base):
    __tablename__ = 'advogados'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)
    telefone = Column(String)  
    
    casos = relationship('Caso', back_populates='advogado', cascade="all, delete-orphan")

class Caso(Base):
    __tablename__ = 'casos'
    
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    data_abertura = Column(Date)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    advogado_id = Column(Integer, ForeignKey('advogados.id'))
    
    cliente = relationship('Cliente', back_populates='casos')
    advogado = relationship('Advogado', back_populates='casos')
    documentos = relationship('Documento', back_populates='caso', cascade="all, delete-orphan")

class Documento(Base):
    __tablename__ = 'documentos'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    conteudo = Column(String)
    caso_id = Column(Integer, ForeignKey('casos.id'))
    
    caso = relationship('Caso', back_populates='documentos')
