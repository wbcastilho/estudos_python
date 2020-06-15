from DAO.conexao import Conexao

class Cliente():
    def __init__(self, **kwargs):        
        self._nome = kwargs['nome'] if 'nome' in kwargs else None
        self._idade = kwargs['idade'] if 'idade' in kwargs else None

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade

class ClienteBLL():
    def __init__(self):
       pass
   
    @staticmethod
    def listar():
        db = Conexao.conectar()
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM cliente")
            print(cursor.fetchall())
        finally:
            db.close()
   
    def inserir(self, cliente):
        db = Conexao.conectar()
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO cliente(nome, idade) VALUES (%s, %s)", (cliente.nome, cliente.idade))
            db.commit()
        finally:
            db.close()
   
    def editar(self, id, cliente):
        db = Conexao.conectar()
        try:
            cursor = db.cursor()
            cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE id=%(id)s",
                       ({'nome': cliente.nome, 'idade': cliente.idade, 'id': id}))
            db.commit()
        finally:
            db.close()
   
    def remover(self, id):
        db = Conexao.conectar()
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM cliente WHERE id=%s", (id,))
            db.commit()
        finally:
            db.close()