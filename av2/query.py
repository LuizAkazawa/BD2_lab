class Queries:
    def __init__(self, database):
        self.db = database

    def get_info_teacher(self, name):
        query = "MATCH (a:Teacher {name: $name}) RETURN a.ano_nasc, a.cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["a.ano_nasc"], result["a.cpf"]) for result in results]

    def get_teachers_start_m(self):
        query = "MATCH (a:Teacher) WHERE a.name STARTS WITH $prefix RETURN a.name, a.cpf"
        parameters = {"prefix": "M"}
        results = self.db.execute_query(query, parameters)
        return [(result["a.name"], result["a.cpf"]) for result in results]

    def get_cities(self):
        query = "MATCH (a:City) RETURN a.name"
        results = self.db.execute_query(query)
        return [(result["a.name"]) for result in results]

    def get_schools_range(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= $minimo AND s.number <= $maximo
        RETURN s.name, s.address, s.number
        """
        parameters = {"minimo": 150, "maximo": 550}
        results = self.db.execute_query(query, parameters)
        return [(result["s.name"], result["s.address"], result["s.number"]) for result in results]

    def get_youngest_oldest_teacher(self):
        query = """
        MATCH (t:Teacher)
        RETURN MAX(t.ano_nasc) AS youngest_ano, MIN(t.ano_nasc) AS oldest_ano
        """
        results = self.db.execute_query(query)
        return results[0]["youngest_ano"], results[0]["oldest_ano"]

    def get_average_population(self):
        query = """
        MATCH (c:City)
        RETURN AVG(c.population) AS average_population
        """
        results = self.db.execute_query(query)
        return results[0]["average_population"]

    def get_nome_cidade(self):
        query = """
        MATCH (c:City {cep: "37540-000"})
        RETURN REPLACE(c.name, 'a', 'A') AS modified_name
        """
        results = self.db.execute_query(query)
        #print("results = ", results)
        return results[0]["modified_name"]

    def get_terceira_letra(self):
        query = """
        MATCH (t:Teacher)
        RETURN LEFT(SUBSTRING(t.name, 2), 1) AS third_letter
        """
        results = self.db.execute_query(query)
        return [result["third_letter"] for result in results]




