import mysql.connector, configparser

class Conexao():

    @staticmethod
    def conectar():       
        config = configparser.ConfigParser()
        config.read('DAO/config.ini')
        db = mysql.connector.connect(
            host=config['DATABASE']['host'],
            user=config['DATABASE']['user'],
            password=config['DATABASE']['passwd'],
            database=config['DATABASE']['db']                       
        )

        return db