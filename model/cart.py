

from sys import maxsize

class Cart:
    def __init__(self, customer=None, product=None, qty=None, price=None):
        self.customer = customer
        self.product = product
        self.qty = qty
        self.price = price




    def __repr__(self):
        return "%s:%s:%s:%s" % (self.customer, self.product, self.qty, self.price)



    def __eq__(self, other):
        return self.customer == other.customer and self.product == other.product and self.qty == other.qty and self.price == other.price


    def sort_by_id(self):
        return self.customer and self.product