import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import logo from "./logo.svg";
import "./Homepage.css";

export default function Homepage() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Link to="/recipes-list">
          <h2>Recipes list</h2>
        </Link>
      </header>
    </div>
  );
}
