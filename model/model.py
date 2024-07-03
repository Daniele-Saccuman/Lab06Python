from database.products_dao import ProductsDao
from database.retailers_dao import RetailersDao
from database.sales_dao import SalesDao
from model.retailer import Retailer


class Model:
    def __init__(self):
        self._sales_dao = SalesDao()
        self._products_dao = ProductsDao()
        self._retailers_dao = RetailersDao()
        self.retailers_map = {}

    def get_anni(self):
        return self._sales_dao.get_anno()

    def get_brands(self):
        return self._products_dao.get_brand()

    def get_retailers(self) -> set[Retailer]:
        return self._retailers_dao.get_retailers(self.retailers_map)

    def get_top_sales(self, anno, brand, retailer_code):
        filtered_sales = self._sales_dao.get_filtered_sales(anno, brand, retailer_code)
        filtered_sales.sort(reverse=True)
        return filtered_sales[0:5]

    def get_sales_stats(self, anno, brand, retailer_code):
        """
            Funzione che legge dal dal dao le vendite con i filtri selezionati,
            e ne restituisce le prime 5 (se presenti) ordinate per ricavo decrescente
        """
        filtered_sales = self._sales_dao.get_filtered_sales(anno, brand, retailer_code)
        ricavo_totale = sum([sale.ricavo for sale in filtered_sales])
        retailers_involved = set([sale.retailer_code for sale in filtered_sales])
        product_involved = set([sale.product_number for sale in filtered_sales])
        return ricavo_totale, len(filtered_sales), len(retailers_involved), len(product_involved)