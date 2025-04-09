import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
    return (
        <div>
            <div className="darksouls-separator"></div>
            <h1>404 - Страница не найдена</h1>
            <div className="darksouls-separator"></div>
            <p>К сожалению, запрашиваемая страница не существует.</p>
            <Link to="/main" className="darksouls-flame">Вернуться на главную</Link>
        </div>
    );
};

export default NotFoundPage;
