from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Models go here!


db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    reviews = db.relationship('Review', backref = 'user')
    restaurants = association_proxy('reviews', 'restaurant')



class Restaurant(db.Model, SerializerMixin):
    __tablename__ ='restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    reviews = db.relationship('Review', backref = 'restaurant')
    users = association_proxy('reviews', 'user')

    @validates('location')
    def validate_location(self, key, location):
        locations = ['North','South', 'East', 'West']
        if location not in locations:
            raise ValueError('must be valid location')
        return location


class Review(db.Model, SerializerMixin):
    __tablename__ ='reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    rating_ = db.Column(db.Integer)
    review = db.Column(db.String)
    img = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    @validates('location')
    def validate_location(self, key, location):
        locations = ['North','South', 'East', 'West']
        if location not in locations:
            raise ValueError('must be valid location')
        return location