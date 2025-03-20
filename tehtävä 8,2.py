import mysql.connector
from win32comext.mapi.mapi import MAPI_E_UNABLE_TO_ABORT

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Ammar1108',
    collation='utf8_general_ci',
    autocommit=True
    )
def lentokentat(maa_koodi):
    query = (f"SELECT count(typy) FROM airport "
             f"WHERE iso_country = '{maa_koodi}' GROUP BY type")
    kursori.execute(query)
    palautus = kurdori.fetchall()
    for rivi in palautus:
        print(f"{rivi[0]}')

