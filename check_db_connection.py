
## check connection with database

from model.users import User
import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="opencart", user="root", password="")

# try:
#     cursor = connection.cursor()
#     cursor.execute("select customer_id, firstname, lastname,email, telephone from oc_customer")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

user_list =[]
try:
    cursor = connection.cursor()
    cursor.execute("select customer_id, firstname, lastname, email, telephone from oc_customer")
    for row in cursor:
        (id, firstname, lastname, email, telephone) = row
        user_list.append(User(id=id, firstname=firstname, lastname=lastname, username=email, phone=telephone))
    print(user_list)
    print(len(user_list))
finally:
    connection.close()