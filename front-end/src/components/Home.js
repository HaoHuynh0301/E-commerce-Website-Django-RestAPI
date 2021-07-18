import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Home extends Component {
    constructor(props) {
        super(props);

    }

    render() {
        return (
            <div>
                 <main>
                    <div className="container">
                        {/*Section: Products v.3*/}
                        <section className="text-center mb-4">
                            {/*Grid row*/}
                            <div className="row wow fadeIn">
                                {/*Grid column*/}
                                <div className="col-lg-3 col-md-6 mb-4">
                                    {/*Card*/}
                                    <div className="card">
                                    {/*Card image*/}
                                    <div className="view overlay">
                                        <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/12.jpg" className="card-img-top" alt="" />
                                        <a>
                                        <div className="mask rgba-white-slight" />
                                        </a>
                                    </div>
                                    {/*Card image*/}
                                    {/*Card content*/}
                                    <div className="card-body text-center">
                                        {/*Category & Title*/}
                                        <a href className="grey-text">
                                        <h5>Shirt</h5>
                                        </a>
                                        <h5>
                                        <strong>
                                            <a href className="dark-grey-text">Denim shirt
                                            <span className="badge badge-pill danger-color">NEW</span>
                                            </a>
                                        </strong>
                                        </h5>
                                        <h4 className="font-weight-bold blue-text">
                                        <strong>120$</strong>
                                        </h4>
                                    </div>
                                    {/*Card content*/}
                                    </div>
                                    {/*Card*/}
                                </div>
                                {/*Grid column*/}
                                {/*Grid column*/}
                                <div className="col-lg-3 col-md-6 mb-4">
                                    {/*Card*/}
                                    <div className="card">
                                    {/*Card image*/}
                                    <div className="view overlay">
                                        <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/13.jpg" className="card-img-top" alt="" />
                                        <a>
                                        <div className="mask rgba-white-slight" />
                                        </a>
                                    </div>
                                    {/*Card image*/}
                                    {/*Card content*/}
                                    <div className="card-body text-center">
                                        {/*Category & Title*/}
                                        <a href className="grey-text">
                                        <h5>Sport wear</h5>
                                        </a>
                                        <h5>
                                        <strong>
                                            <a href className="dark-grey-text">Sweatshirt</a>
                                        </strong>
                                        </h5>
                                        <h4 className="font-weight-bold blue-text">
                                        <strong>139$</strong>
                                        </h4>
                                    </div>
                                    {/*Card content*/}
                                    </div>
                                    {/*Card*/}
                                </div>
                                {/*Grid column*/}
                                {/*Grid column*/}
                                <div className="col-lg-3 col-md-6 mb-4">
                                    {/*Card*/}
                                    <div className="card">
                                    {/*Card image*/}
                                    <div className="view overlay">
                                        <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/14.jpg" className="card-img-top" alt="" />
                                        <a>
                                        <div className="mask rgba-white-slight" />
                                        </a>
                                    </div>
                                    {/*Card image*/}
                                    {/*Card content*/}
                                    <div className="card-body text-center">
                                        {/*Category & Title*/}
                                        <a href className="grey-text">
                                        <h5>Sport wear</h5>
                                        </a>
                                        <h5>
                                        <strong>
                                            <a href className="dark-grey-text">Grey blouse
                                            <span className="badge badge-pill primary-color">bestseller</span>
                                            </a>
                                        </strong>
                                        </h5>
                                        <h4 className="font-weight-bold blue-text">
                                        <strong>99$</strong>
                                        </h4>
                                    </div>
                                    {/*Card content*/}
                                    </div>
                                    {/*Card*/}
                                </div>
                                {/*Grid column*/}
                                {/*Fourth column*/}
                                <div className="col-lg-3 col-md-6 mb-4">
                                    {/*Card*/}
                                    <div className="card">
                                    {/*Card image*/}
                                    <div className="view overlay">
                                        <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/15.jpg" className="card-img-top" alt="" />
                                        <a>
                                        <div className="mask rgba-white-slight" />
                                        </a>
                                    </div>
                                    {/*Card image*/}
                                    {/*Card content*/}
                                    <div className="card-body text-center">
                                        {/*Category & Title*/}
                                        <a href className="grey-text">
                                        <h5>Outwear</h5>
                                        </a>
                                        <h5>
                                        <strong>
                                            <a href className="dark-grey-text">Black jacket</a>
                                        </strong>
                                        </h5>
                                        <h4 className="font-weight-bold blue-text">
                                        <strong>219$</strong>
                                        </h4>
                                    </div>
                                    {/*Card content*/}
                                    </div>
                                    {/*Card*/}
                                </div>
                                {/*Fourth column*/}
                            </div>
                            {/*Grid row*/}
                        </section>
                        {/*Section: Products v.3*/}
                        {/*Pagination*/}
                        <nav className="d-flex justify-content-center wow fadeIn">
                            <ul className="pagination pg-blue">
                            {/*Arrow left*/}
                            <li className="page-item disabled">
                                <a className="page-link" href="#" aria-label="Previous">
                                <span aria-hidden="true">«</span>
                                <span className="sr-only">Previous</span>
                                </a>
                            </li>
                            <li className="page-item active">
                                <a className="page-link" href="#">1
                                <span className="sr-only">(current)</span>
                                </a>
                            </li>
                            <li className="page-item">
                                <a className="page-link" href="#">2</a>
                            </li>
                            <li className="page-item">
                                <a className="page-link" href="#">3</a>
                            </li>
                            <li className="page-item">
                                <a className="page-link" href="#">4</a>
                            </li>
                            <li className="page-item">
                                <a className="page-link" href="#">5</a>
                            </li>
                            <li className="page-item">
                                <a className="page-link" href="#" aria-label="Next">
                                <span aria-hidden="true">»</span>
                                <span className="sr-only">Next</span>
                                </a>
                            </li>
                            </ul>
                        </nav>
                        {/*Pagination*/}
                    </div>
                </main>
            </div>
        );
    }
}
export default Home;