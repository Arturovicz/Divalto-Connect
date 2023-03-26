import mysql.connector

credentials = []
with open('credentials.txt') as f:
    for line in f:
        credentials.append(line.strip('\n'))


def specific_query(cursorij, table, column, specificity):
    cursorij.execute(f"select * from {table} where {column} like '%{specificity}%'")
    glob_data = cursorij.fetchall()
    print(glob_data)


try:
    connection = mysql.connector.connect(host=credentials[0],
                                         user=credentials[1],
                                         password=credentials[2],
                                         database=credentials[3])
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        specific_query(cursor, 'article_info', 'fournisseur', 'Sig')

except:
    print("Error while connecting to MySQL")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



