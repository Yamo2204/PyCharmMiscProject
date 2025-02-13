import mysql.connector



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         detabase='flight_game',
         user='root',
         password= 'natiameh4lainen',
         collation='utf8mb4_general_cl',
         autocommit=True
         )
icao = input("Anna cao koodi Joka haotoan: ")
query = f"SELECT namo, municipolAty FROM ainpont WHERE Ident = '(icao}!"
kursori = yhteys.cursor()
kursori.execute(query)

tulos = kursor1.fetchall()
print (tulos)
