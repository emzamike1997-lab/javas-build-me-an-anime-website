```python
from flask import Blueprint, request, jsonify
from models import Anime, Genre
from schemas import AnimeSchema, GenreSchema
from app import db

anime_blueprint = Blueprint('anime', __name__)
genre_blueprint = Blueprint('genre', __name__)

# Anime routes
@anime_blueprint.route('/animes', methods=['GET'])
def get_animes():
    """Returns a list of all anime entries."""
    animes = Anime.query.all()
    anime_schema = AnimeSchema(many=True)
    return jsonify(anime_schema.dump(animes))

@anime_blueprint.route('/animes/<int:id>', methods=['GET'])
def get_anime(id):
    """Returns a single anime entry by ID."""
    anime = Anime.query.get(id)
    if anime is None:
        return jsonify({'error': 'Anime not found'}), 404
    anime_schema = AnimeSchema()
    return jsonify(anime_schema.dump(anime))

@anime_blueprint.route('/animes', methods=['POST'])
def create_anime():
    """Creates a new anime entry."""
    data = request.get_json()
    anime_schema = AnimeSchema()
    errors = anime_schema.validate(data)
    if errors:
        return jsonify({'error': 'Invalid data'}), 400
    anime = Anime(title=data['title'], description=data['description'], genre_id=data['genre_id'])
    db.session.add(anime)
    db.session.commit()
    return jsonify(anime_schema.dump(anime)), 201

@anime_blueprint.route('/animes/<int:id>', methods=['PUT'])
def update_anime(id):
    """Updates an existing anime entry."""
    anime = Anime.query.get(id)
    if anime is None:
        return jsonify({'error': 'Anime not found'}), 404
    data = request.get_json()
    anime_schema = AnimeSchema()
    errors = anime_schema.validate(data)
    if errors:
        return jsonify({'error': 'Invalid data'}), 400
    anime.title = data['title']
    anime.description = data['description']
    anime.genre_id = data['genre_id']
    db.session.commit()
    return jsonify(anime_schema.dump(anime))

@anime_blueprint.route('/animes/<int:id>', methods=['DELETE'])
def delete_anime(id):
    """Deletes an anime entry."""
    anime = Anime.query.get(id)
    if anime is None:
        return jsonify({'error': 'Anime not found'}), 404
    db.session.delete(anime)
    db.session.commit()
    return jsonify({'message': 'Anime deleted'})

# Genre routes
@genre_blueprint.route('/genres', methods=['GET'])
def get_genres():
    """Returns a list of all genres."""
    genres = Genre.query.all()
    genre_schema = GenreSchema(many=True)
    return jsonify(genre_schema.dump(genres))

@genre_blueprint.route('/genres/<int:id>', methods=['GET'])
def get_genre(id):
    """Returns a single genre by ID."""
    genre = Genre.query.get(id)
    if genre is None:
        return jsonify({'error': 'Genre not found'}), 404
    genre_schema = GenreSchema()
    return jsonify(genre_schema.dump(genre))

@genre_blueprint.route('/genres', methods=['POST'])
def create_genre():
    """Creates a new genre."""
    data = request.get_json()
    genre_schema = GenreSchema()
    errors = genre_schema.validate(data)
    if errors:
        return jsonify({'error': 'Invalid data'}), 400
    genre = Genre(name=data['name'], description=data['description'])
    db.session.add(genre)
    db.session.commit()
    return jsonify(genre_schema.dump(genre)), 201

@genre_blueprint.route('/genres/<int:id>', methods=['PUT'])
def update_genre(id):
    """Updates an existing genre."""
    genre = Genre.query.get(id)
    if genre is None:
        return jsonify({'error': 'Genre not found'}), 404
    data = request.get_json()
    genre_schema = GenreSchema()
    errors = genre_schema.validate(data)
    if errors:
        return jsonify({'error': 'Invalid data'}), 400
    genre.name = data['name']
    genre.description = data['description']
    db.session.commit()
    return jsonify(genre_schema.dump(genre))

@genre_blueprint.route('/genres/<int:id>', methods=['DELETE'])
def delete_genre(id):
    """Deletes a genre."""
    genre = Genre.query.get(id)
    if genre is None:
        return jsonify({'error': 'Genre not found'}), 404
    db.session.delete(genre)
    db.session.commit()
    return jsonify({'message': 'Genre deleted'})
```