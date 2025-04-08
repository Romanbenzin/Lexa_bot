import React, { useState } from 'react';

const MainPage = () => {
    const [purchaseCount, setPurchaseCount] = useState(null);
    const [pingMessage, setPingMessage] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const getPurchaseCount = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('/api/count_purchases');
            const data = await response.json();
            setPurchaseCount(data.purchase_count);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const ping = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('/api/ping');
            const data = await response.json();
            setPingMessage(data.message);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <div className="darksouls-separator"></div>
            <h1>Lexa_bot</h1>
            <div className="darksouls-separator"></div>
            <button onClick={getPurchaseCount} className="darksouls-flame">Получить количество покупок</button>
            <button onClick={ping} className="darksouls-flame">Проверить работу API (ping)</button>
            <div className="darksouls-separator"></div>
            <div id="result">
                {loading && <p>Загрузка...</p>}
                {error && <p style={{ color: 'red' }}>{error}</p>}
                {!loading && !error && (
                    <div>
                        {purchaseCount !== null && <p>Количество покупок: <strong>{purchaseCount}</strong></p>}
                        {pingMessage !== null && <p>Ответ сервера: <strong>{pingMessage}</strong></p>}
                    </div>
                )}
            </div>
        </div>
    );
};

export default MainPage;
