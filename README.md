# Late Show API

A Flask API for managing episodes, guests, and appearances of a late-night talk show. This API allows you to retrieve episode and guest information, as well as create new guest appearances.

## Features

- Get a list of all episodes
- Get details of a specific episode including guest appearances
- Get a list of all guests
- Create new guest appearances with ratings

## Technologies Used

- Python 3.8+
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd late-show-api-flask
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate sqlalchemy-serializer
```

4. Set up the database:
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Seed the database with initial data:
```bash
python server/seed.py
```

## Running the Application

Start the Flask development server:
```bash
python -m server.app
```

The server will start on `http://localhost:5555`.

## API Endpoints

### GET /episodes
Returns a list of all episodes.

Response format:
```json
[
    {
        "id": 1,
        "date": "1/11/99",
        "number": 1
    }
]
```

### GET /episodes/:id
Returns details of a specific episode.

Response format:
```json
{
    "id": 1,
    "date": "1/11/99",
    "number": 1,
    "appearances": [
        {
            "episode_id": 1,
            "guest": {
                "id": 1,
                "name": "Michael J. Fox",
                "occupation": "actor"
            },
            "guest_id": 1,
            "id": 1,
            "rating": 4
        }
    ]
}
```

### GET /guests
Returns a list of all guests.

Response format:
```json
[
    {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
    }
]
```

### POST /appearances
Creates a new guest appearance.

Request format:
```json
{
    "rating": 5,
    "episode_id": 1,
    "guest_id": 1
}
```

Response format:
```json
{
    "id": 1,
    "rating": 5,
    "guest_id": 1,
    "episode_id": 1,
    "episode": {
        "date": "1/11/99",
        "id": 1,
        "number": 1
    },
    "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
    }
}
```

## Data Models

### Episode
- id: Integer (Primary Key)
- date: String
- number: Integer
- appearances: Relationship to Appearance model

### Guest
- id: Integer (Primary Key)
- name: String
- occupation: String
- appearances: Relationship to Appearance model

### Appearance
- id: Integer (Primary Key)
- rating: Integer (1-5)
- episode_id: Integer (Foreign Key)
- guest_id: Integer (Foreign Key)

## Validation Rules

- Appearance ratings must be between 1 and 5 (inclusive)
- Episode and Guest must exist before creating an Appearance

## Project Structure
```
late-show-api-flask/
│
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── seed.py
│
├── instance/
│   └── late_show.db
│
├── migrations/
├── seed.csv
├── README.md
└── requirements.txt
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:
- 200: Successful GET request
- 201: Successful POST request
- 404: Resource not found
- 400: Invalid request (e.g., invalid rating)
- 500: Server error

## Development

1. Make sure to activate the virtual environment before working on the project:
```bash
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. After making changes to the models, create and apply migrations:
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## Testing

Use Postman or curl to test the API endpoints. Example curl commands:

```bash
# Get all episodes
curl http://localhost:5555/episodes

# Get specific episode
curl http://localhost:5555/episodes/1

# Get all guests
curl http://localhost:5555/guests

# Create new appearance
curl -X POST http://localhost:5555/appearances \
  -H "Content-Type: application/json" \
  -d '{"rating": 5, "episode_id": 1, "guest_id": 1}'
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Contact
Alex Maragia - maragialex@gmail.com
Project Link: [([(https://github.com/alexmaragia/late-show-api-flask.git)](https://github.com/alexmaragia/late-show-api-flask.git))]