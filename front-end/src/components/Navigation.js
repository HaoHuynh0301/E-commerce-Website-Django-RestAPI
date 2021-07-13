import React, { useState } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
  } from "react-router-dom";
// import Modal from "react-bootstrap/Modal";

class Navigation extends React.Component {
    render() {
        return (
            <div>
                <nav id="side-nav">
                    <i className="fas fa-bars"/>
                    <div className="side-nav">
                        <a className="close" onClick=""><i class="far fa-window-close"></i></a>
                        <Link to="#">Home</Link>
                        <Link to="#">Shop</Link>
                        <Link to="#">Contact</Link>
                        <Link to="#">News</Link>
                    </div>
                </nav>
            </div>
        );
    }
}

export default Navigation;
