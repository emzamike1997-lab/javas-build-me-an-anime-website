```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import AnimeList from './AnimeList';
import Header from './Header';
import Footer from './Footer';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import AnimeDetails from './AnimeDetails';

function App() {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path="/" element={<AnimeList />} />
                <Route path="/anime/:id" element={<AnimeDetails />} />
            </Routes>
            <Footer />
        </BrowserRouter>
    );
}

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
```

###