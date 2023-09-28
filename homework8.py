'''
import mysql.connector

db = mysql.connector.connect(
    host = "192.168.1.17",
    port = 3306,
    database = "flight_game",
    user = "dbuser",
    password = "admin",
    autocommit = True
)

def getAirportNameAndLocationByICAO(icao: str) -> ():
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'";
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return (result[0], result[1])

icao = str(input("Please provide the ICAO code to fetch the airport details: "))
name, city = getAirportNameAndLocationByICAO(icao)

print(f"Airport name: {name}\nCity: {city}")



import mysql.connector

db = mysql.connector.connect(
    host = "192.168.1.17",
    port = 3306,
    database = "flight_game",
    user = "dbuser",
    password = "admin",
    autocommit = True
)

def getAirportsByCountryOrderByType(countrycode: str) -> []:
    sql = f"SELECT name, type FROM airport WHERE iso_country='{countrycode}' ORDER BY type;"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

country = str(input("Please provide country code: "))
airports = getAirportsByCountryOrderByType(country)


for airport in airports:
    print(f"Name: {airport[0]}\nType: {airport[1]}\n")



import mysql.connector
from geopy import distance

db = mysql.connector.connect(
    host = "192.168.1.17",
    port = 3306,
    database = "flight_game",
    user = "dbuser",
    password = "admin",
    autocommit = True
)

def getAirportCoordinates(icao: str) -> ():
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def calculateDistance(coordinates1: tuple, coordinates2: tuple) -> float:
    return distance.distance(coordinates1, coordinates2).km

airport1 = str(input("Enter first airport icao: "))
airport2 = str(input("Enter second airport icao: "))

print(f"The distance between airports is {calculateDistance(getAirportCoordinates(airport1), getAirportCoordinates(airport2))}")

'''