from database import Database

class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create_teacher(self, name, ano_nasc, cpf):
        query = "CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf }
        self.db.execute_query(query, parameters)
        print("PROFESSOR CRIADO")

    def read_teacher(self, name):
        query ="MATCH (t:Teacher {name: $name}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        print("RETORNANDO PROFESSOR")
        return results

    def delete_teacher(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print("PROFESSOR DELETADO")

    def update_teacher(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
        print("CPF DO PROFESSOR ATUALIZADO")