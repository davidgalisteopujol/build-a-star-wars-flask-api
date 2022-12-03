from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique = False, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    fav_characters = db.relationship('People', secondary='fav_characters', lazy='subquery', backref=db.backref('user', lazy=True))
    fav_planets = db.relationship('Planet', secondary='fav_planets', lazy='subquery', backref=db.backref('user', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email,
            # "fav_characters": self.fav_characters,
            # "fav_planets": self.fav_planets
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    description = db.Column(db.String(250), nullable = False) 
    height = db.Column(db.Integer, nullable = False)
    mass = db.Column(db.Integer, nullable = True)
    hair_color = db.Column(db.String(250), nullable = True)
    skin_color = db.Column(db.String(250), nullable = True)
    eye_color = db.Column(db.String(250), nullable = True)	
    birthday_year = db.Column(db.Integer, nullable = True)
    Gender = db.Column(db.String(250), nullable = True)

    def serialize_people(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "height": self.height
        }


class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    description = db.Column(db.String(250), nullable = False) 
    diameter = db.Column(db.Integer, nullable = False)
    rotation_period = db.Column(db.Integer, nullable = True)
    orbital_period = db.Column(db.Integer, nullable = True)
    gravity = db.Column(db.String(250), nullable = True)
    population = db.Column(db.Integer, nullable = True)
    climate = db.Column(db.String(250), nullable = True)
    terrain = db.Column(db.String(250), nullable = True)
    surface_water = db.Column(db.Integer, nullable = True)

    def serialize_planet(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "diameter": self.diameter
        }


fav_characters = db.Table('fav_characters',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True)
)

fav_planets = db.Table('fav_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'), primary_key=True)
)


