from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('metacritic', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Review(BaseModel):
    name = CharField()
    platform = CharField()
    developer = CharField()
    publisher = CharField()
    genre = CharField()
    players = CharField()
    rating = CharField()
    release_date = CharField()
    link = CharField()
    metascore = IntegerField()


db.connect()
db.drop_tables([Review])
db.create_tables([Review])


Review(name='Command & Conquer', platform='PC', developer='Westwood Studios', publisher='Virgin Interactive', genre='Sci-Fi', players='1-4', rating='T', release_date='Aug 31, 1995', link='/game/pc/command-conquer', metascore=47).save()
# Command & Conquer,PC,Westwood Studios,Virgin Interactive,Sci-Fi,1-4 ,T,,"Aug 31, 1995",/game/pc/command-conquer,5,0,0,94,47,0,1,8.9