

from sys import maxsize

class Cart:
    def __init__(self, customer=None, product=None, price=None, qty=None):
        self.customer = customer
        self.product = product
        self.price = price
        self.qty = qty



    def __repr__(self):
        return "%s:%s:%s:%s" % (self.customer, self.product, self.price, self.qty)



    def __eq__(self, other):
        return self.customer == other.customer and self.product == other.product


    # def id_or_max(self):
    #     if self.id:
    #         return int(self.id)
    #     else:
    #         return maxsize