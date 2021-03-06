# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('tibia.db')
# definindo um cursor
cursor = conn.cursor()

#INSERIR CAST**

#Dropando tabela (CASO TENHA NECESSIDADE)
cursor.execute("""
Drop TABLE top_distance 
""")
conn.commit()
print('Tabela dropada com sucesso.')


# criando a tabela top_distance (schema)
cursor.execute("""
CREATE TABLE top_distance (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    Rank INTEGER  NULL,
    Name VARCHAR(30)  NULL,
    Vocation VARCHAR(20)  NULL,
    Level INTEGER  NULL,
    World VARCHAR(25)  NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
conn.commit()
print('Tabela top_distance criada com sucesso.')


# desconectando...
conn.close()
