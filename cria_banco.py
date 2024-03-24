import sqlite3

# Conectando no banco de dados
connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

# Criando a tabela
criar_tabela = '''
CREATE TABLE IF NOT EXISTS 
hoteis (
    hotel_id text PRIMARY KEY, 
    nome text, 
    estrelas real, 
    diaria real, 
    cidade text)
'''

# adicionando um hotel
hotel = '''
INSERT INTO hoteis VALUES (
    "alpha", 
    "Alpha Hotel", 
    4.3, 
    345.30, 
    "Rio de Janeiro")
'''

# Executando a criação da tabela
cursor.execute(criar_tabela)
cursor.execute(hotel)
connection.commit()
connection.close()