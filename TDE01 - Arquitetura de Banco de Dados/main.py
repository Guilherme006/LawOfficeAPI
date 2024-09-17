from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from database import SessionLocal, engine, Base
import json
from handlers import (
    # Handlers de Cliente
    create_cliente, get_clientes, get_cliente,
    update_cliente, delete_cliente,
    # Handlers de Advogado
    create_advogado, get_advogados, get_advogado,
    update_advogado, delete_advogado,
    # Handlers de Caso
    create_caso, get_casos, get_caso,
    update_caso, delete_caso,
    # Handlers de Documento
    create_documento, get_documentos, get_documento,
    update_documento, delete_documento,
    # Função de Utilidade
    parse_request_body
)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        session = SessionLocal()
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        try:
            if len(path_parts) == 1:
                entity = path_parts[0]
                if entity == "clientes":
                    clientes = get_clientes(session)
                    self._set_headers()
                    self.wfile.write(json.dumps(clientes).encode())
                elif entity == "advogados":
                    advogados = get_advogados(session)
                    self._set_headers()
                    self.wfile.write(json.dumps(advogados).encode())
                elif entity == "casos":
                    casos = get_casos(session)
                    self._set_headers()
                    self.wfile.write(json.dumps(casos).encode())
                elif entity == "documentos":
                    documentos = get_documentos(session)
                    self._set_headers()
                    self.wfile.write(json.dumps(documentos).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
            elif len(path_parts) == 2:
                entity, entity_id = path_parts
                if entity == "clientes":
                    response, status = get_cliente(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "advogados":
                    response, status = get_advogado(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "casos":
                    response, status = get_caso(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "documentos":
                    response, status = get_documento(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        finally:
            session.close()

    def do_POST(self):
        session = SessionLocal()
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        try:
            if len(path_parts) == 1:
                entity = path_parts[0]
                data = parse_request_body(self)

                if entity == "clientes":
                    response, status = create_cliente(session, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "advogados":
                    response, status = create_advogado(session, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "casos":
                    response, status = create_caso(session, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "documentos":
                    response, status = create_documento(session, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        finally:
            session.close()

    def do_PUT(self):
        session = SessionLocal()
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        try:
            if len(path_parts) == 2:
                entity, entity_id = path_parts
                data = parse_request_body(self)

                if entity == "clientes":
                    response, status = update_cliente(session, entity_id, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "advogados":
                    response, status = update_advogado(session, entity_id, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "casos":
                    response, status = update_caso(session, entity_id, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "documentos":
                    response, status = update_documento(session, entity_id, data)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        finally:
            session.close()

    def do_DELETE(self):
        session = SessionLocal()
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        try:
            if len(path_parts) == 2:
                entity, entity_id = path_parts

                if entity == "clientes":
                    response, status = delete_cliente(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "advogados":
                    response, status = delete_advogado(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "casos":
                    response, status = delete_caso(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                elif entity == "documentos":
                    response, status = delete_documento(session, entity_id)
                    self._set_headers(status)
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        finally:
            session.close()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
