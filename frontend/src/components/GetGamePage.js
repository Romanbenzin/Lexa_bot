import React, { useState } from 'react';

const GetGamePage = () => {
    const [games, setGames] = useState([]);
    const [userName, setUserName] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const getGames = async () => {
        if (!userName) {
            setError('Введите имя пользователя');
            return;
        }
        setLoading(true);
        setError(null);
        try {
            const response = await fetch(`/api/get_game?user_name=${encodeURIComponent(userName)}`);
            const data = await response.json();
            if (Array.isArray(data)) {
                setGames(data);
            } else if (data.message) {
                setGames([]);
                setError(data.message);
            } else {
                throw new Error('Неизвестный формат ответа');
            }
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <div className="darksouls-separator"></div>
            <h1>Список игр</h1>
            <div className="darksouls-separator"></div>
            <input value={userName} onChange={(e) => setUserName(e.target.value)} placeholder="Введите имя пользователя" />
            <button onClick={getGames} className="darksouls-flame">Получить список игр</button>
            <div id="result">
                {loading && <p>Загрузка...</p>}
                {error && <p style={{ color: 'red' }}>{error}</p>}
                {!loading && !error && (
                    <ul>
                        {games.map((game, index) => (
                            <li key={index}>
                                <a href={game.game_link} target="_blank" rel="noopener noreferrer">{game.game_name}</a> ({game.purchase_date})
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
};

export default GetGamePage;
