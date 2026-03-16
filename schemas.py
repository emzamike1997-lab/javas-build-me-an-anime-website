```python
from marshmallow import Schema, fields

class AnimeSchema(Schema):
    """Represents an anime entry."""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    genre_id = fields.Int(required=True)

class GenreSchema(Schema):
    """Represents a genre."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
```