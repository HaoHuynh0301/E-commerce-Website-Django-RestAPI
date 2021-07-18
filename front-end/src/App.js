import React, { Component, Button, Modal, useState } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';
import Navigation from './components/Navigation.js'
import Footer from './components/Footer.js'
import Wrapper from './components/Wrapper.js'
import Home from './components/Home.js'

function App() {
  return (
    <Router>
      <div>
        <Navigation />
        <Wrapper/>
        <Switch>
          <Route to="/home"> 
            <Home />
          </Route>
        </Switch>
        <Footer />
      </div>
    </Router>
    
  );
}

export default App;
