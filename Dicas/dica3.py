# Funções só devem retornar um tipo de retorno

# Maneira errada
# Caso users seja false irá retornar None e com isso esta função terá dois retornos
def get_user(username):    
    users = User(username=username).select()
    if users:
        return users.first()

# Maneira correta
def get_user(username):   
    users = User(username=username).select()
    if not users:
        raise UserNotFoundError(f"{username} does not exist.")  # Gera uma exceção
    return users.first()

# Maneira correta
# com type anotations
# e comentários que aparecem na descrição da chamada da função
def get_user(username: str) -> User:
    """Query user by its username
    :param username: A str holding username
    :returns: User instance
    :raises: UserNotFoundError
    """
    users = User(username=username).select()
    if not users:
        raise UserNotFoundError(f"{username} does not exist.")  # Gera uma exceção
    return users.first()