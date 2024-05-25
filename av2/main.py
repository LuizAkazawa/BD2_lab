from database import Database
from query import Queries
from cli import TeacherCLI
from CRUD import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.203.186.103:7687", "neo4j", "saving-removals-appraisals")
#db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
queries_db = Queries(db)
'''
EXERCICIO 1:

x1 = queries_db.get_info_teacher("Renzo")
x2 = queries_db.get_teachers_start_m()
x3 = queries_db.get_cities()
x4 = queries_db.get_schools_range()

print(x1)
print(x2)
print(x3)
print(x4)

=============================================

EXERCICIO 2
y1 = queries_db.get_youngest_oldest_teacher()
y2 = queries_db.get_average_population()
y3 = queries_db.get_nome_cidade()
y4 = queries_db.get_terceira_letra()

print(y1)
print(y2)
print(y3)
print(y4)

=========================================

EXERCICIO 3

TeacherC = TeacherCRUD(db)

TeacherC.create_teacher("Chris Lima", 1956, "189.052.396-66")

TeacherC.delete_teacher("Chris Lima")

z1 = TeacherC.read_teacher("Chris Lima")
print(z1)

TeacherC.update_teacher("Chris Lima", "162.052.777-77")
z2 = TeacherC.read_teacher("Chris Lima")
print(z2)

'''
TeacherCRUD = TeacherCRUD(db)
TeacherCli = TeacherCLI(TeacherCRUD)
TeacherCli.run()

# Fechando a conexão com o banco de dados
db.close()