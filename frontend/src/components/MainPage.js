import React, { useState } from 'react';

const MainPage = () => {
    const [purchaseCount, setPurchaseCount] = useState(null);
    const [pingMessage, setPingMessage] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const makeApiRequest = async (url, options = {}) => {
        setLoading(true);
        setError(null);
        try {
            const defaultHeaders = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            };

            const response = await fetch(url, {
                ...options,
                headers: {
                    ...defaultHeaders,
                    ...(options.headers || {})
                },
                credentials: 'include' // если нужна передача кук/аутентификация
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const getPurchaseCount = async () => {
        try {
            const data = await makeApiRequest('/api/count_purchases');
            setPurchaseCount(data.purchase_count);
            setPingMessage(null); // Сбрасываем предыдущее сообщение ping
        } catch {
            setPurchaseCount(null);
        }
    };

    const ping = async () => {
        try {
            const data = await makeApiRequest('/api/ping');
            setPingMessage(data.message);
            setPurchaseCount(null); // Сбрасываем предыдущее количество покупок
        } catch {
            setPingMessage(null);
        }
    };

    return (
        <div>
            <div className="darksouls-separator"></div>
            <h1>Lexa_bot</h1>
            <div className="darksouls-separator"></div>
            <button 
                onClick={getPurchaseCount} 
                className="darksouls-flame"
                disabled={loading}
            >
                Получить количество покупок
            </button>
            <button 
                onClick={ping} 
                className="darksouls-flame"
                disabled={loading}
            >
                Проверить работу API (ping)
            </button>
            <div className="darksouls-separator"></div>
            <div id="result">
                {loading && <p>Загрузка...</p>}
                {error && <p style={{ color: 'red' }}>{error}</p>}
                {!loading && !error && (
                    <div>
                        {purchaseCount !== null && (
                            <p>Количество покупок: <strong>{purchaseCount}</strong></p>
                        )}
                        {pingMessage !== null && (
                            <p>Ответ сервера: <strong>{pingMessage}</strong></p>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
};

export default MainPage;