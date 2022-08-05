from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    gravity = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "image": self.image,
            "gravity": self.gravity,
            } 
class Character(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(250), nullable=False)
        gender = db.Column(db.String(10), nullable=False)
        homeworld = db.Column(db.String(100), nullable=False)
        image = db.Column(db.String(100), nullable=False)

        def __repr__(self):
            return '<Character %r>' % self.name

        def serialize(self):
            return {
                "id": self.id,
                "name": self.name,
                "gender": self.gender,
                "image": self.image,
                "homeworld": self.homeworld,
        }
class Starship(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(250), nullable=False)
        image = db.Column(db.String(100), nullable=False)
        model = db.Column(db.String(100), nullable=False)
        length = db.Column(db.String(100), nullable=False)

        def __repr__(self):
            return '<Starship %r>' % self.name

        def serialize(self):
            return {
                "id": self.id,
                "name": self.name,
                "model": self.model,
                "image": self.image,
                "length": self.length
        }
class Favorite(db.Model):
        __tablename__ = 'favorite'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User')
        starship_id = db.Column(db.Integer, db.ForeignKey('starship.id'))
        starship = db.relationship('Starship')
        character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
        character = db.relationship('Character')
        planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
        planet = db.relationship('Planet')

        def __repr__(self):
            return '<Favorite %r>' % self.id

        def serialize(self):
            return {
                "id": self.id,
                "user": self.user,
                "starship_id": self.starship_id,
                "character_id": self.character_id,
                "planet_id": self.planet_id
        }