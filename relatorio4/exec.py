from database import Database
from helper.writeAJson import writeAJson


class ProductAnalyzer():

    def vendas_dia(self):
        db = Database(database="mercado", collection="compras")
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id.data": 1, "total": -1}}
        ])
        writeAJson(result, "Total de vendas por dia")

    def prod_maisVendido(self):
        db = Database(database="mercado", collection="compras")
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendas": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendas": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")

    def mais_gasto(self):
        db = Database(database="mercado", collection="compras")
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": "$produtos.preco"}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Mais gasto em uma unica compra")

    def listar_produtos_vendidos(self):
        db = Database(database="mercado", collection="compras")
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 1}}},
            {"$group": {"_id": "$produtos.descricao",}},
            {"$project": {"_id": 0, "produto": "$_id"}}
        ])
        writeAJson(result, "Produtos vendidos listados")
