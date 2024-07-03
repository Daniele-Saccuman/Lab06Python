from database.DB_connect import DBConnect
from model.product import Product


class ProductsDao:

    def get_brand(self) -> list[tuple[str]]:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT gp.Product_brand
                FROM go_products gp"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    def getAllProducts(self) -> set[Product]:
        conn = DBConnect.get_connection()

        result = set()

        cursor = conn.cursor(dictionary=True)
        query = """select * from go_products"""

        cursor.execute(query)

        for row in cursor:
            result.add(Product(row["Product_number"],
                                   row["Product_line"],
                                   row["Product_type"],
                                   row["Product"],
                                   row["Product_brand"],
                                   row["Product_color"],
                                   row["Unit_cost"],
                                   row["Unit_price"]))

        cursor.close()
        conn.close()
        return result

