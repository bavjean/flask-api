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

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/game', methods=['GET', 'POST'])
@app.route('/game/<id>', methods=['GET', 'PUT', 'DELETE'])
def game(id=None):
    if request.method == 'GET':
        if id:
            review_model = Review.get(Review.id == id)
            review_dictionary = model_to_dict(review_model)
            return jsonify(review_dictionary)
        else:
            return 'GET request'

    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        return 'POST request'

    if request.method == 'DELETE':
        return 'DELETE request'

app.run(port=9000, debug=True)