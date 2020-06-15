#import cliente, cliente_repositorio
from BLL.cliente import Cliente
from BLL.cliente import ClienteBLL

cliente = Cliente()
cliente.nome = "Rogério"
cliente.idade = 32
repositorio = ClienteBLL()
repositorio.inserir(cliente)
#repositorio.editar(3, cliente)
#repositorio.remover(14)

repositorio.listar()