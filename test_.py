def pract_mysql():
    import mysql.connector

    mydb = mysql.connector.connect(host='localhost', user='root', passwd='root')
    
    cursor = mydb.cursor()
    cursor.execute("use students")

    cursor.execute("select * from students")
    result = cursor.fetchall()
    # result = cursor.fetchone()
    for i in result:
        print(i)

pract_mysql()
