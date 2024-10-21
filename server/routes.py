from flask import jsonify, request, make_response
from . import app
from .models import db, Episode, Guest, Appearance

# get all episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': episode.id,
        'date': episode.date,
        'number': episode.number
    } for episode in episodes])

# get a specific episode by id
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    return make_response(jsonify({"error": "Episode not found"}), 404)

# get all guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    } for guest in guests])

# create a new appearance
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.json
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except ValueError as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"errors": ["An error occurred while creating the appearance"]}), 500)

# test route to verify the app is working
@app.route('/', methods=['GET'])
def hello():
    return "Hello, Late Show API!"