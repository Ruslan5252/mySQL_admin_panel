import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="ruslan"

)

mycursor = mydb.cursor()

while True:
    print("PRESS 1 TO INSERT PRODUCTS")
    print("PRESS 2 TO LIST PRODUCTS")
    print("PRESS 3 TO UPDATE PRODUCTS")
    print("PRESS 4 TO DELETE PRODUCTS")
    print("PRESS 0 TO EXIT")

    choice = input()

    if choice == "1":
        try:
            print("select the table where you want to insert the data")
            print(
                "if you want to insert data into the products table , press 1\n"
                "if you want to insert data into the PC table , press 2")
            choice_add = input("Your choice ")
            if choice_add == "1":
                print("INSERT NAME:")
                name = input()
                print("INSERT NUMBER:")
                number = int(input())
                print("INSERT PRICE:")
                price = int(input())

                sql = "INSERT INTO products (id, name, number, price) VALUES (NULL , %s, %s, %s) "
                values = (name, number, price)
                mycursor.execute(sql, values)
                mydb.commit()
            elif choice_add == "2":
                print("INSERT MODEL_PC:")
                model_pc = input()
                print("INSERT TYPE:")
                type = input()
                print("INSERT RAM:")
                ram = int(input())
                sql = "INSERT INTO pc (id_pc, model_pc, type, ram) VALUES (NULL , %s, %s, %s) "
                values = (model_pc, type, ram)
                mycursor.execute(sql, values)
                mydb.commit()
        except:
            print("one or more fields to fill in are missing")

    elif choice == "2":

        print("select the table where you want to list the data")
        print(
            "if you want to list data into the products table , press 1\nif you want to list data into the PC table , press 2")
        choice_list = input("Your choice ")
        if choice_list == "1":
            sql = "SELECT * FROM products"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for player in result:
                print(str(player[0]) + " " + player[1] + " " + str(player[2]) + " " + str(player[3]))

        elif choice_list == "2":
            sql = "SELECT * FROM pc"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for PC in result:
                print(str(PC[0]) + " " + PC[1] + " " + PC[2] + " " + str(PC[3]))
    elif choice == "3":
        try:
            print("select the table where you want to update the data")
            print(
                "if you want to update data into the products table , press 1\nif you want to update data into the PC table , press 2")
            choice_update1 = input("Your choice ")
            if choice_update1 == "1":
                print("select the criteria by which you want to update the field")
                print(
                    "if you want to update by id press 1\nif you want to update by name press 2\n")
                choice_update = input("Your choice ")
                if choice_update == "1":
                    print("INSERT ID WHICH YOU WANT UPDATE")
                    id = int(input())
                    print("INSERT NEW NAME:")
                    new_name = input()
                    print("INSERT NEW NUMBER:")
                    new_number = int(input())
                    print("INSERT NEW PRICE:")
                    new_price = int(input())
                    sql = "UPDATE products SET name = %s , number = %s, price = %s where id =" + str(id)
                    val = (new_name, new_number, new_price)
                    mycursor.execute(sql, val)
                    mydb.commit()
                elif choice_update == "2":
                    print("INSERT name WHICH YOU WANT UPDATE")
                    name = int(input())
                    print("INSERT NEW NAME:")
                    new_name = input()
                    print("INSERT NEW NUMBER:")
                    new_number = int(input())
                    print("INSERT NEW PRICE:")
                    new_price = int(input())
                    sql = "UPDATE products SET name = %s , number = %s, price = %s where name =" + str(name)
                    val = (new_name, new_number, new_price)
                    mycursor.execute(sql, val)
                    mydb.commit()
            elif choice_update1 == "2":
                print("select the criteria by which you want to update the field")
                print(
                    "if you want to update by Id_pc press 1\nif you want to update by model_pc press 2\n")
                choice_update = input("Your choice ")
                if choice_update == "1":
                    print("INSERT ID_PC WHICH YOU WANT UPDATE")
                    id_pc = int(input())
                    print("INSERT NEW MODEL_PC")
                    new_model_pc = input()
                    print("INSERT NEW TYPE")
                    new_type = input()
                    print("INSERT NEW RAM")
                    new_ram = int(input())
                    sql = "UPDATE pc SET model_pc = %s,type = %s, ram = %s where id_pc = " + str(id_pc)
                    val = (new_model_pc, new_type, new_ram)
                    mycursor.execute(sql, val)
                    mydb.commit()
                elif choice_update == "2":
                    print("INSERT model_pc WHICH YOU WANT UPDATE")
                    model_pc = input()
                    print("INSERT NEW MODEL_PC")
                    new_model_pc = input()
                    print("INSERT NEW TYPE")
                    new_type = input()
                    print("INSERT NEW RAM")
                    new_ram = int(input())
                    sql = "UPDATE pc SET model_pc = %s,type = %s, ram = %s where model_pc = " + str(model_pc)
                    val = (new_model_pc, new_type, new_ram)
                    mycursor.execute(sql, val)
                    mydb.commit()
        except:
            print("one or more fields to fill in are missing")
    elif choice == "4":
        print("select the table where you want to delete the data")
        print(
            "if you want to delete data from the products table , press 1\nif you want to delete data from the PC table , press 2")
        choice_delete1 = input("Your choice ")
        if choice_delete1 == "1":

            print("select the criteria by which you want to delete the field")
            print(
                "if you want to delete by Id press 1\nif you want to delete by name press 2\nif you want to clear table press 3")
            choice_delete = input("Your choice ")
            if choice_delete == '1':
                print("INSERT ID WHICH YOU WANT DELETE")
                id = int(input())
                sql = "DELETE FROM products where id=" + str(id)
                mycursor.execute(sql)
                mydb.commit()
            elif choice_delete == '2':
                print("INSERT NAME WHICH YOU WANT DELETE")
                name = input()
                sql = "DELETE FROM products where name=" + str(name)
                mycursor.execute(sql)
                mydb.commit()
            elif choice_delete == '3':
                sql = "DELETE FROM products"
                sql1 = "ALTER TABLE products AUTO_INCREMENT=1"
                mycursor.execute(sql)
                mycursor.execute(sql1)
                mydb.commit()

        elif choice_delete1 == "2":

            print("select the criteria by which you want to delete the field")
            print(
                "if you want to delete by Id press 1\nif you want to delete by model press 2\nif you want to clear table press 3")
            choice_delete = input("Your choice ")
            if choice_delete == '1':
                print("INSERT ID_PC WHICH YOU WANT DELETE")
                id_pc = int(input())
                sql = "DELETE FROM pc where id_pc=" + str(id_pc)
                mycursor.execute(sql)
                mydb.commit()
            elif choice_delete == '2':
                print("INSERT MODEL_PC WHICH YOU WANT DELETE")
                model_pc = input()
                sql = "DELETE FROM pc WHERE model_pc=" + str(model_pc)
                mycursor.execute(sql)
                mydb.commit()
            elif choice_delete == '3':
                sql = "DELETE FROM pc"
                sql1 = "ALTER TABLE pc AUTO_INCREMENT=1"
                mycursor.execute(sql)
                mycursor.execute(sql1)
                mydb.commit()

    elif choice == "0":
        mycursor.close()
        mydb.disconnect()
        break
