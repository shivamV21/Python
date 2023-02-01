def first():
    print('~' * 160)
    print('~' * 66, 'FOOD ORDERING AND DELIVERY', '~' * 66)
    print('~' * 160)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat do you want to do?")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1) USER LOGIN ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2) ORDER FOOD ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3) GRAPHICS ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4) EXIT APPLICATION ")
    print('~' * 160)
    print('~' * 160)

###################################### creting connection between python and oracle ####################################

    import cx_Oracle
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    connection = cx_Oracle.connect(user="system", password="1234", dsn="localhost/XE")
    cursor = connection.cursor()

    userinput = int(input("Enter your choice(1-4):"))

##################################################### USER LOGIN PAGE ##################################################

    if userinput == 1:

        def insert_customer(cid, cname, caddress, carea, ccontact):
            cursor.execute("insert into customer(cid, cname, caddress, carea, ccontact) values(:1,:2,:3,:4,:5)",
                           (cid, cname, caddress, carea, ccontact))
            cursor.close()
            connection.commit()

        try:
            q = int(input("Enter Customer id:"))
            if (q >= 6001 and q <= 6030):
                print('User aldready exist')

            else:
                w = input("Enter Customer name:")
                e = input("Enter Customer address:")
                r = input("Enter Customer's area:")
                t = input("Enter Customer contact no.:")

                insert_customer(q, 'w', 'e', 'r',t)
                print("Congrats!! You are successfully registered on our application")

            sql = ("select * from customer where cid = :abcd")
            cursor.execute(sql, abcd=q)
            res = cursor.fetchall()
            df = pd.DataFrame(res, columns=['Cid', 'Cname', 'Caddress', 'carea','contact'])
            print(df)


        except Exception as e:
            print(e)
        first()




##################################################### ORDER FOOD ######################################################

    if userinput == 2:
        print("Select a shop to see its menu")
        cursor.execute(
            """
            Select * from shop
            """
        )
        res = cursor.fetchall()
        df = pd.DataFrame(res, columns=['Shop_Id', 'Shop_Name', 'Area', 'Address', 'Rating', 'Contact', 'Did'])
        print(df)


######################################################### MENU DISPLAY #################################################



        shopinput = input("Enter shop name: ")
        sql = (
            "select a.shopid, a.shopname, b.pid, b.pname, b.pprice, b.veg_nonveg from menu b, shop a "
            "where a.shopid = b.shopid AND shopname = :a")
        cursor.execute(sql, a=shopinput)
        res = cursor.fetchall()
        df = pd.DataFrame(res, columns=['Shop_Id', 'Shop_Name', 'pid', 'pname', 'pprice', 'veg_nonveg'])
        print(df)



######################################################### MENU Selecting ##############################################



        menuinput = input("Enter what do you want to order: ")
        menuinpu = input("Enter what do you want to order: ")
        sql = ("select a.shopid, a.shopname, b.pid, b.pname, b.pprice, b.veg_nonveg from menu b, shop a "
               "where a.shopid = b.shopid AND shopname = :a AND (pname = :b OR pname = :z)")
        cursor.execute(sql, a=shopinput, b=menuinput, z = menuinpu)
        res = cursor.fetchall()
        df = pd.DataFrame(res, columns=['Shop_Id', 'Shop_Name', 'pid', 'pname', 'pprice', 'veg_nonveg'])
        print(df)



        a1 = input("Please enter your customer ID: ")



        print("Congrats. Your order is successfully placed!!!")
        print("Your order will be delivered to this address within 30 minitues!!")
        sql = ("select caddress, carea from customer where cid = :c")
        cursor.execute(sql, c=a1)
        res = cursor.fetchall()
        df = pd.DataFrame(res, columns=['Address', 'area'])
        print(df)
        first()





######################################################## GRAPHICS ####################################################



    if userinput == 3:

        print("1. Number of veg and non veg items.")
        print("2. Number of number of shops by area.")


        cursor.execute("select veg_nonveg, count(veg_nonveg) from menu group by veg_nonveg")
        goes = []
        rows = []
        for row in cursor:
            goes.append(row[0])
            rows.append(row[1])
        plt.pie(rows, labels=goes, shadow=True)
        plt.show()



        cursor.execute("select area, count(area) from shop group by area")
        goes = []
        rows = []
        for row in cursor:
            goes.append(row[0])
            rows.append(row[1])
        plt.pie(rows, labels=goes, shadow=True)
        plt.show()
        first()

##################################################### EXIT APPLICATION #################################################

    if userinput == 4:
        print("Thnak you for using our application")
        exit()

################################################## Calling the entire frnction #########################################

first()