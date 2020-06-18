from flask import Flask, request, jsonify
from peewee import *
from datetime import date
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('metacritic', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Reviews(BaseModel):
    name: CharField()
    platform: CharField()
    developer: CharField()
    publisher: CharField()
    genre(s): CharField()
    players: CharField()
    rating: CharField()
    release_date: DateField()
    link: CharField()
    metascore: IntegerField()


db.connect()
db.drop_tables([Reviews])
db.create_tables([Reviews])