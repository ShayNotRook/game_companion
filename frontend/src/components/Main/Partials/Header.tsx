import React from 'react';

import './Header.css';

const Header: React.FC = () => {
  return (
    <header className='header'>
        <div className='header-content'>
            <div className='logo'>
                <img src="/Logo-s.svg" alt="LudoVerse Logo" className="logo-icon"/>
                <img src="/Logo-text-2.svg" alt="LudoVerse" className='logo-text' />
            </div>
            <nav className='nav'>
                <ul className='nav-links'>
                    <li>
                        <a href="/games">Games</a>
                    </li>
                    <li>
                        <a href="/about">About Us</a>
                    </li>
                    <li>
                        <a href="/contact">Contact</a>
                    </li>
                </ul>
            </nav>
        </div>
    </header>
  )
}

export default Header