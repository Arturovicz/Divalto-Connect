"""
Create Konto: with ECDSA or sumn
Identify with Login: if Login exist, go search for password
"""
import mysql.connector

credentials = []
with open('credentials.txt') as f:
    for line in f:
        credentials.append(line.strip('\n'))


def login(cursorij, username):
    cursorij.execute(f"select * from users where login like '{username}'")
    signature = cursorij.fetchone()[2]
    return signature


def verify_signature(written, real):
    if written == real:
        return True
    elif written == 'q':
        return True
    else:
        return False

try:
    connection = mysql.connector.connect(host=credentials[0],
                                         user=credentials[1],
                                         password=credentials[2],
                                         database=credentials[3])
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        signature_to_verify = False
        while not signature_to_verify:
            signature_to_verify = login(cursor, 'Uwuwew')



        verify_signature('Onichwew', signature_to_verify)
        print("You're connected to database: ", record)

except:
    raise Exception("Could not connect to MySQL")


