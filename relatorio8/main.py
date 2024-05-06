from database import Database
from school_database import SchoolDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.85.228.25:7687", "neo4j", "possession-buzzes-pieces")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
soccer_db = SchoolDatabase(db)

# Criando alguns jogadores
soccer_db.create_jogador("João", "J1") #FLA
soccer_db.create_jogador("Maria", "J2") #FLA
soccer_db.create_jogador("Pedro", "J3") #FLA
soccer_db.create_jogador("Ana", "J4") #FLU
soccer_db.create_jogador("Luiz", "J5") #FLU
soccer_db.create_jogador("Clara", "J6") #FLU
soccer_db.create_jogador("Miguel", "J7") #CRU
soccer_db.create_jogador("Sofia", "J8") #CRU
soccer_db.create_jogador("Lucas", "J9") #CRU



# Criando algumas partidas
soccer_db.create_partida("Fla x Flu", "Azul", "P1")
soccer_db.create_partida("Fla x Cru", "Azul", "P2")
soccer_db.create_partida("Cru x Flu", "Vermelho", "P3")

#Definindo relações partida FLA x FLU
soccer_db.create_jogador_partida("Fla x Flu","João", 3, "Azul")
soccer_db.create_jogador_partida("Fla x Flu","Maria", 0, "Azul")
soccer_db.create_jogador_partida("Fla x Flu","Pedro", 1, "Azul")
soccer_db.create_jogador_partida("Fla x Flu","Ana", 1, "Vermelho")
soccer_db.create_jogador_partida("Fla x Flu","Luiz", 1, "Vermelho")
soccer_db.create_jogador_partida("Fla x Flu","Clara", 1, "Vermelho")

#Definindo relações partida FLA x CRU
soccer_db.create_jogador_partida("Fla x Cru","João", 0, "Azul")
soccer_db.create_jogador_partida("Fla x Cru","Maria", 1, "Azul")
soccer_db.create_jogador_partida("Fla x Cru","Pedro", 0, "Azul")
soccer_db.create_jogador_partida("Fla x Cru","Miguel", 0, "Vermelho")
soccer_db.create_jogador_partida("Fla x Cru","Sofia", 0, "Vermelho")
soccer_db.create_jogador_partida("Fla x Cru","Lucas", 0, "Vermelho")

#Definindo relações partida Cru x Flu
soccer_db.create_jogador_partida("Cru x Flu","Miguel", 0, "Azul")
soccer_db.create_jogador_partida("Cru x Flu","Sofia", 0, "Azul")
soccer_db.create_jogador_partida("Cru x Flu","Lucas", 0, "Azul")
soccer_db.create_jogador_partida("Cru x Flu","Ana", 0, "Vermelho")
soccer_db.create_jogador_partida("Cru x Flu","Luiz", 1, "Vermelho")
soccer_db.create_jogador_partida("Cru x Flu","Clara", 1, "Vermelho")

#PRINTANDO INFO SOBRE O DATABASE
print()
print("Jogadores:")
print(soccer_db.get_jogadores())
print()
print("Info partida específica: ")
print(soccer_db.get_info_partidas("Fla x Flu"))
print()
print("Relações")
print(soccer_db.get_relacoes())
print()

#BUSCANDO PARTIDA ESPECIFICA

#historico de jogador especifico
print(soccer_db.historico_jogador('Luiz'))
print()


# Fechando a conexão com o banco de dados
db.close()