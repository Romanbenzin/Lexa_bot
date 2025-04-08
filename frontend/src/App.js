import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import MainPage from './components/MainPage';
import GetGamePage from './components/GetGamePage';
import NotFoundPage from './components/NotFoundPage';
import './App.css';

const App = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    const closeMenu = () => {
        setIsMenuOpen(false);
    };

    return (
        <Router basename="/main"> {/* Добавляем basename */}
            <div>
                <button className="menu-toggle" onClick={toggleMenu}>☰</button>
                <div id="sidebar" className={isMenuOpen ? 'active' : ''}>
                    <div className="menu-content">
                        <Link to="/main" className="menu-link" onClick={closeMenu}>Главная</Link>
                        <Link to="/get_game" className="menu-link" onClick={closeMenu}>Список игр</Link>
                    </div>
                </div>
                <div id="main-content">
                    <Routes>
                        <Route path="/main" element={<MainPage />} />
                        <Route path="/get_game" element={<GetGamePage />} />
                        <Route path="*" element={<NotFoundPage />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
};

export default App;
