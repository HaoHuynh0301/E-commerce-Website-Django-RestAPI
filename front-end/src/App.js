import React, { Component, Button, Modal, useState } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';
import Navigation from './components/Navigation.js'

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <Switch>
          
        </Switch>
      </div>
    </Router>
    
  );
}

export default App;
