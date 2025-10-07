import React from 'react';
import { Link } from 'react-router-dom';
import logo from '@/assets/logo.png';

const Header = () => {
  return (
    <header className="bg-background border-b sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4">
        <Link to="/" className="flex items-center gap-3">
          <img src={logo} alt="Innovative Mentor Pool" className="h-8 w-auto" />
          <span className="text-xl font-bold text-primary">Innovative Mentor Pool</span>
        </Link>
      </div>
    </header>
  );
};

export default Header;