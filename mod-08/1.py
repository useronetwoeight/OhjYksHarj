'''
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
'''

import mysql.connector

bamse = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    passwd='bamse',
    autocommit=True
    )


def get_airport_by_icao(icao):
    sql = 'select name, municipality, type FROM airport WHERE ident = "{icao}"'
    cursor = bamse.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    return result


icao = input("cacao")

'''
def get_airport_by_name(name):
    sql = 'select'

with bamse.cursor() as cursor:
    print()

print(f'nimi {airport[0][0]}" joka sijaitsee kunnassa " {airport[0][1]}')
'''

airport = get_airport_by_icao(icao)
print(airport)

for ap in airport:
    print(f'nimi {ap[0]} joka sijaitsee kunasa {ap[1]}')

