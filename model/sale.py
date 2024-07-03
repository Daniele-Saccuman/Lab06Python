
from datetime import datetime
from dataclasses import dataclass

from model.product import Product
from model.retailer import Retailer


@dataclass
class Sale:
    date: datetime.date
    quantity: int
    unit_price: float
    unit_sale_price: float

    #relazioni
    retailer_code: int
    Product_number: int
    order_method_code: int
    retailer: Retailer = None
    product: Product = None

    def __post_init__(self):
        self.ricavo: float = self.unit_sale_price * self.quantity

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Product: {self.Product_number}"

    def __eq__(self, other):
        return (self.retailer_code == other.retailer_code
                and self.Product_number == other.Product_number
                and self.order_method_code == other.order_method_code)

    def __hash__(self):
        return hash((self.retailer_code, self.Product_number, self.order_method_code))

    def __lt__(self, other):
        return self.ricavo < other.ricavo