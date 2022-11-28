from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique = False, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email,
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

# class Favorites(db.Model):
#     __tablename__ = "favorites"
#     id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     user = db.relationship("User")
#     character_id = db.Column(db.Integer, db.ForeignKey("people.id"))
#     character = db.relationship("People")
#     planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
#     planet = db.relationship("Planet")

#     def serialize_favorites(self):
#          return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "character_id": self.character_id,
#             "planet_id": self.planet_id,
#         }

class Favorites_people(db.Model):
    __tablename__ = "favorites_people"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
    character_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    character = db.relationship("People")
    

    def serialize_favorites_people(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }


class Favorites_planets(db.Model):
    __tablename__ = "favorites_planets"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet")

    def serialize_favorites_planets(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
