import csv
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

with open('metacritic_games.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Review(name=row['name'], platform=row['platform'], developer=row['developer'], publisher=row['publisher'], genre=row['genre(s)'], players=row['players'], rating=row['rating'], release_date=row['release_date'], link=row['link'], metascore=row['metascore']).save()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Metacritic reviews'

@app.route('/game', methods=['GET', 'POST'])
@app.route('/game/<id>', methods=['GET', 'PUT', 'DELETE'])
def game(id=None):
    if request.method == 'GET':
        if id:
            review_model = Review.get(Review.id == id)
            review_dictionary = model_to_dict(review_model)
            return jsonify(review_dictionary)
        else:
            review_list = []
            for review in Review.select():
                review_list.append(model_to_dict(review))
            return jsonify(review_list)

    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        return 'POST request'

    if request.method == 'DELETE':
        return 'DELETE request'

app.run(port=9000, debug=True)