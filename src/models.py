from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=False, nullable=False)
    birth_year = db.Column(db.Integer, unique=False, nullable=False)
    eye_color = db.Column(db.String(256), unique=False, nullable=False)
    gender = db.Column(db.String(256), unique=False, nullable=False)
    hair_color = db.Column(db.String(256), unique=False, nullable=False)
    height = db.Column(db.String(256), unique=False, nullable=False)
    weight = db.Column(db.String(256), unique=False, nullable=False)
    complexion = db.Column(db.String(256), unique=False, nullable=False)
    url = db.Column(db.String(256), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "weight": self.weight,
            "complexion": self.complexion,
            "url": self.url,

            
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=False, nullable=False)
    diameter = db.Column(db.String(256), unique=False, nullable=False)
    rotation_period = db.Column(db.String(256), unique=False, nullable=False)
    oribital_period = db.Column(db.String(256), unique=False, nullable=False)
    gravity = db.Column(db.String(256), unique=False, nullable=False)
    population = db.Column(db.String(256), unique=False, nullable=False)
    climate = db.Column(db.String(256), unique=False, nullable=False)
    terrain = db.Column(db.String(256), unique=False, nullable=False)
    surface_water = db.Column(db.String(256), unique=False, nullable=False)
    url = db.Column(db.String(256), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "oribital_period": self.oribital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "url": self.url,
        }