import React, { useState } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
  } from "react-router-dom";
import Modal from "react-bootstrap/Modal";
import axiosInstance from '../axios.js';

function SignUpAlert(message) {
    if(message === 'signup') alert('Create account successfully !');
    alert('Sign in successfully !');
}

function Navigation() {

    // declare for modal
    const [isOpen, setIsOpen] = React.useState(false);
    const [isOpenSignUp, setIsOpenSignUp] = React.useState(false);

    const showModal = () => {
        setIsOpen(true);
        setIsOpenSignUp(false);
      };
    
    const hideModal = () => {
        setIsOpen(false);
    };

    const showModalSignUp = () => {
        setIsOpenSignUp(true);
        setIsOpen(false)
      };
    
    const hideModalSignUp = () => {
        setIsOpenSignUp(false);
    };

    // declare for signup and SignUp handle

    const initialFormData = Object.freeze({
        email: '',
        user_name: '',
        first_name: '',
        password: ''
    });
    const [formData, updateFormData] = useState(initialFormData);
    const handleChange = (e) => {
        
        updateFormData({
            ...formData,
            [e.target.name]: e.target.value.trim(),
        });
    };
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('formData');
        axiosInstance
            .post('api/user/register/', {
                email: formData.email,
                user_name: formData.username,
                first_name: formData.firstname,
                password: formData.password,
            })
            .then(() => {
                console.log('OK');
                SignUpAlert('signup');  
                showModal();
            });
    };

    const intialSignInFormData = Object.freeze({
        email: '',
        password: ''
    });
    const [formSignInData, updateSignInFormData] = useState(intialSignInFormData);
    const handleSignInChange = (e) => {
        updateSignInFormData({
            ...formSignInData,
            [e.target.name]: e.target.value.trim(),
        });
    };
    const handleSignInSubmit = (e) => {
        e.preventDefault();
        console.log('formData');
        axiosInstance
            .post('token/', {
                email: formSignInData.email,
                password: formSignInData.password
            })
            .then((res) => {
                localStorage.setItem('access-token', res.data.access);
                localStorage.setItem('refresh-token', res.data.refresh);
                axiosInstance.defaults.headers['Authorization'] = 
                    'JWT' + localStorage.getItem('access-token');
                SignUpAlert('signin'); 
                hideModal();
            }).catch((err) => {
                console.log(err);
            });
    };

    return (
        <div>
                <nav className="navbar fixed-top navbar-expand-lg navbar-light white scrolling-navbar">
                <div className="container">
                    <Link className="navbar-brand waves-effect" to="/home" >
                        <strong className="blue-text">Yame</strong>
                    </Link>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav mr-auto">
                        <li className="nav-item active">
                            <Link className="nav-link waves-effect" to="/home">Home
                                <span className="sr-only">(current)</span>
                            </Link>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link waves-effect" href="https://www.facebook.com/hulo.bungchay/" target="_blank">About</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link waves-effect" href="#" target="_blank">Contact</a>
                        </li>
                        </ul>
                        <ul className="navbar-nav nav-flex-icons">
                        <li className="nav-item">
                            <a className="nav-link waves-effect">
                            <span className="badge red z-depth-1 mr-1"> 0 </span>
                            <i className="fas fa-shopping-cart" />
                            <span className="clearfix d-none d-sm-inline-block"> Cart </span>
                            </a>
                        </li>
                        <li className="nav-item">
                            <a href="https://www.facebook.com/hulo.bungchay/" className="nav-link waves-effect" target="_blank">
                            <i className="fab fa-facebook-f" />
                            </a>
                        </li>
                        <li className="nav-item">
                            <a href="#" className="nav-link waves-effect" target="_blank">
                            <i className="fab fa-twitter" />
                            </a>
                        </li>
                        <li className="nav-item">
                            <Link onClick={showModal} className="nav-link border border-light rounded waves-effect">
                                Login
                            </Link>
                        </li>
                        </ul>
                    </div>
                </div>
            </nav><hr></hr><hr></hr>

            <Modal show={isOpen} onHide={hideModal}>
                <Modal.Header>
                    <Modal.Title className = 'modal-title'>Sign in to Yame</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                <form noValidate>
                    <input name="email" type="text" className="form-control" placeholder="Email" 
                        onChange = {handleSignInChange}
                        required style={{borderRadius: '50px', marginBottom: '10px'}} />
                    <input name="password" type="password" className="form-control" placeholder="Password"
                        onChange = {handleSignInChange}
                        required style={{borderRadius: '50px', marginBottom: '10px'}} />
                    <button className="btn btn-primary" 
                        onClick = {handleSignInSubmit}
                        style={{borderRadius: '50px', padding: '0.5em', width: '100%', marginBottom: '10px'}}>Sign in</button>
                    <div>New to BlogSite?  <span className=""><Link onClick={showModalSignUp} style={{color: '#00cccc'}} >Create new account</Link></span></div>
                </form>
                </Modal.Body>
            </Modal>

            <Modal show={isOpenSignUp} onHide={hideModalSignUp}>
                <Modal.Header>
                    <Modal.Title className = 'modal-title'>Sign Up to BlogSite</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                <form method="POST" aciton name="sentMessage" id="signUpForm" noValidate>
                    <input name="email" type="text" className="form-control" 
                        onChange={handleChange}
                        placeholder="Email" required style={{borderRadius: '50px', marginBottom: '10px'}} />
                    <input name="username" type="text" className="form-control" placeholder="Username" 
                        onChange={handleChange}
                        required style={{borderRadius: '50px', marginBottom: '10px'}} />
                    <input name="firstname" type="text" className="form-control" placeholder="First Name" 
                        onChange={handleChange}
                        required style={{borderRadius: '50px', marginBottom: '10px'}} />
                    <input name="password" type="password" className="form-control" placeholder="Password" 
                        onChange={handleChange}
                        required style={{borderRadius: '50px', marginBottom: '10px'}} />
                    <button name="submit" type="submit" className="btn btn-primary" 
                        onClick={handleSubmit}
                        style={{borderRadius: '50px', padding: '0.5em', width: '100%', marginBottom: '10px'}}>Sisn up</button>
                    <div>Already have an account?  <span><Link onClick={showModal} style={{color: '#00cccc'}}>Sign in</Link></span></div>
                </form>
                </Modal.Body>
            </Modal>
        </div>
    );
}

export default Navigation;
