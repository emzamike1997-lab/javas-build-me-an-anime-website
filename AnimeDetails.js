```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function AnimeDetails() {
    const { id } = useParams();
    const [anime, setAnime] = useState({});
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get(`https://api.example.com/animes/${id}`)
            .then(response => {
                setAnime(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }, [id]);

    if (error) {
        return (
            <div className="error-message">
                {error}
            </div>
        );
    }

    return (
        <div className="container">
            <h1>{anime.title}</h1>
            <img src={anime.image} alt={anime.title} />
            <p>{anime.description}</p>
        </div>
    );
}

export default AnimeDetails;
```

###