'''

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:n>', methods=['GET'])
def prime_number(n):
    return jsonify({"Number": n, "isPrime": is_prime(n)})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:niklas123@localhost/flight_game'

db = SQLAlchemy(app)


# Define the database model
class Airport(db.Model):
    __tablename__ = 'airport'

    icao = db.Column('ident', db.String, primary_key=True)
    name = db.Column('name', db.String)
    location = db.Column('iso_region', db.String)


# Set up the route
@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    airport = Airport.query.filter_by(icao=icao).first()
    if airport:
        return jsonify({"ICAO": airport.icao, "Name": airport.name, "Location": airport.location})
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
'''