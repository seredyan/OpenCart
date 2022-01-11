import pymysql.cursors
from model.users import User
from model.cart import Cart



class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)




    def get_users_list(self):

        users_list = []

        cursor = self.connection.cursor()
        try:
            cursor.execute("select customer_id, firstname, lastname, email, telephone from oc_customer")
            for row in cursor:
                (id, firstname, lastname, username, phone) = row
                users_list.append(User(id=str(id), firstname=firstname, lastname=lastname, username=username, phone=phone))
        finally:
            cursor.close()
        return users_list





    def get_items_in_cart_list(self):

        items_list = []

        cursor = self.connection.cursor()
        try:
            cursor.execute("select customer_id, product_id, quantity from oc_cart")
            for row in cursor:
                (customer, product, qty) = row
                items_list.append(
                    Cart(customer=customer, product=product, qty=qty))
        finally:
            cursor.close()
        return items_list




    def destroy(self):
        self.connection.close()