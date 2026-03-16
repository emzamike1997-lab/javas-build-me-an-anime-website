```python
from flask import Flask
from routes import anime_blueprint, genre_blueprint
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'
db.init_app(app)

app.register_blueprint(anime_blueprint)
app.register_blueprint(genre_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Application
To run the application, navigate to the project directory and execute the following command:
```bash
python app.py
```
This will start the Flask development server, and you can access the API endpoints by visiting `http://localhost:5000` in your web browser.

### Testing the API
You can test the API using a tool like `curl` or a REST client like Postman. Here are some examples of API requests:

* Get all anime entries: `curl http://localhost:5000/animes`
* Get a single anime entry: `curl http://localhost:5000/animes/1`
* Create a new anime entry: `curl -X POST -H "Content-Type: application/json" -d '{"title": "New Anime", "description": "This is a new anime", "genre_id": 1}' http://localhost:5000/animes`
* Update an existing anime entry: `curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Anime", "description": "This is an updated anime", "genre_id": 1}' http://localhost:5000/animes/1`
* Delete an anime entry: `curl -X DELETE http://localhost:5000/animes/1`

Note: Replace `http://localhost:5000` with the actual URL of your API.