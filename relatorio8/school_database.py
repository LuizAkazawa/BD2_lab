
class SchoolDatabase:
    def __init__(self, database):
        self.db = database

    def create_jogador(self, name, identificador):
        query = "CREATE (:Jogador {name: $name, identificador: $identificador})"
        parameters = {"name": name, "identificador": identificador}
        self.db.execute_query(query, parameters)

    def create_partida(self, name, winner, identificador):
        query = "CREATE (:Partida {name: $name, winner: $winner, identificador: $identificador})"
        parameters = {"name": name, "winner": winner, "identificador": identificador}
        self.db.execute_query(query, parameters)

    def create_jogador_partida(self, name, jogador_name, gols, time):
        query = "MATCH (j:Jogador {name: $jogador_name}), (p:Partida {name: $name}) CREATE (j)-[:PARTICIPOU_DE {gols: $gols, time: $time}]->(p)"
        parameters = {"name": name, "jogador_name": jogador_name, "gols": gols, "time": time}
        self.db.execute_query(query, parameters)

    def historico_jogador(self, name):
        l = list()
        query = "MATCH (j:Jogador {name: $name})-[:PARTICIPOU_DE]->(p:Partida) RETURN p"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        for r in results:
            if r != None:
                l.append(r[0]["name"])
        return l

    def get_jogadores(self):
        query = "MATCH (p:Jogador) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_partidas(self):
        query = "MATCH (a:Partida) RETURN a.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_info_partidas(self, name):
        query = "MATCH (a:Partida{name: $name}) RETURN a.name AS name, a.winner AS winner"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["winner"]) for result in results]

    def get_relacoes(self):
        query = "MATCH (a:Partida)<-[:PARTICIPOU_DE]-(p:Jogador) RETURN a.name AS name, p.name AS jogador_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["jogador_name"]) for result in results]

    def update_jogador(self, old_name, new_name):
        query = "MATCH (p:Jogador {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        

    def delete_jogador(self, name):
        query = "MATCH (p:Jogador {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_partida(self, name):
        query = "MATCH (a:Partida {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_relacao(self, name):
        query = "MATCH (a:Partida {name: $name})<-[:PARTICIPA_DE]-(p:Jogador) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)