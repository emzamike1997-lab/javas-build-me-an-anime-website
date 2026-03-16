```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AnimeList() {
    const [animes, setAnimes] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('https://api.example.com/animes')
            .then(response => {
                setAnimes(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }, []);

    if (error) {
        return (
            <div className="error-message">
                {error}
            </div>
        );
    }

    return (
        <div className="container">
            <h1>Anime List</h1>
            <ul className="anime-list">
                {animes.map(anime => (
                    <li key={anime.id}>
                        <div className="anime-info">
                            <img src={anime.image} alt={anime.title} />
                            <div>
                                <h2>{anime.title}</h2>
                                <p>{anime.description}</p>
                            </div>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default AnimeList;
```

###