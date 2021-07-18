import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Wrapper extends Component {
    constructor(props) {
        super(props);

    }
    render() {
        return (
            <div id="carousel-example-1z" className="carousel slide carousel-fade pt-4" data-ride="carousel">
                {/*Indicators*/}
                <ol className="carousel-indicators">
                <li data-target="#carousel-example-1z" data-slide-to={0} className="active" />
                <li data-target="#carousel-example-1z" data-slide-to={1} />
                <li data-target="#carousel-example-1z" data-slide-to={2} />
                </ol>
                {/*/.Indicators*/}
                {/*Slides*/}
                <div className="carousel-inner" role="listbox">
                {/*First slide*/}
                <div className="carousel-item active">
                    <div className="view" style={{backgroundImage: 'url("https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/8-col/img%282%29.jpg")', backgroundRepeat: 'no-repeat', backgroundSize: 'cover'}}>
                    {/* Mask & flexbox options*/}
                    <div className="mask rgba-black-strong d-flex justify-content-center align-items-center">
                        {/* Content */}
                        <div className="text-center white-text mx-5 wow fadeIn">
                        <h1 className="mb-4">
                            <strong>Learn Bootstrap 4 with MDB</strong>
                        </h1>
                        <p>
                            <strong>Best &amp; free guide of responsive web design</strong>
                        </p>
                        <p className="mb-4 d-none d-md-block">
                            <strong>The most comprehensive tutorial for the Bootstrap 4. Loved by over 500 000 users. Video and
                            written versions
                            available. Create your own, stunning website.</strong>
                        </p>
                        <a target="_blank" href="https://mdbootstrap.com/education/bootstrap/" className="btn btn-outline-white btn-lg">Start
                            free tutorial
                            <i className="fas fa-graduation-cap ml-2" />
                        </a>
                        </div>
                        {/* Content */}
                    </div>
                    {/* Mask & flexbox options*/}
                    </div>
                </div>
                {/*/First slide*/}
                {/*Second slide*/}
                <div className="carousel-item">
                    <div className="view" style={{backgroundImage: 'url("https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/8-col/img%283%29.jpg")', backgroundRepeat: 'no-repeat', backgroundSize: 'cover'}}>
                    {/* Mask & flexbox options*/}
                    <div className="mask rgba-black-strong d-flex justify-content-center align-items-center">
                        {/* Content */}
                        <div className="text-center white-text mx-5 wow fadeIn">
                        <h1 className="mb-4">
                            <strong>Learn Bootstrap 4 with MDB</strong>
                        </h1>
                        <p>
                            <strong>Best &amp; free guide of responsive web design</strong>
                        </p>
                        <p className="mb-4 d-none d-md-block">
                            <strong>The most comprehensive tutorial for the Bootstrap 4. Loved by over 500 000 users. Video and
                            written versions
                            available. Create your own, stunning website.</strong>
                        </p>
                        <a target="_blank" href="https://mdbootstrap.com/education/bootstrap/" className="btn btn-outline-white btn-lg">Start
                            free tutorial
                            <i className="fas fa-graduation-cap ml-2" />
                        </a>
                        </div>
                        {/* Content */}
                    </div>
                    {/* Mask & flexbox options*/}
                    </div>
                </div>
                {/*/Second slide*/}
                {/*Third slide*/}
                <div className="carousel-item">
                    <div className="view" style={{backgroundImage: 'url("https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/8-col/img%285%29.jpg")', backgroundRepeat: 'no-repeat', backgroundSize: 'cover'}}>
                    {/* Mask & flexbox options*/}
                    <div className="mask rgba-black-strong d-flex justify-content-center align-items-center">
                        {/* Content */}
                        <div className="text-center white-text mx-5 wow fadeIn">
                        <h1 className="mb-4">
                            <strong>Learn Bootstrap 4 with MDB</strong>
                        </h1>
                        <p>
                            <strong>Best &amp; free guide of responsive web design</strong>
                        </p>
                        <p className="mb-4 d-none d-md-block">
                            <strong>The most comprehensive tutorial for the Bootstrap 4. Loved by over 500 000 users. Video and
                            written versions
                            available. Create your own, stunning website.</strong>
                        </p>
                        <a target="_blank" href="https://mdbootstrap.com/education/bootstrap/" className="btn btn-outline-white btn-lg">Start
                            free tutorial
                            <i className="fas fa-graduation-cap ml-2" />
                        </a>
                        </div>
                        {/* Content */}
                    </div>
                    {/* Mask & flexbox options*/}
                    </div>
                </div>
                {/*/Third slide*/}
                </div>
                {/*/.Slides*/}
                {/*Controls*/}
                <a className="carousel-control-prev" href="#carousel-example-1z" role="button" data-slide="prev">
                <span className="carousel-control-prev-icon" aria-hidden="true" />
                <span className="sr-only">Previous</span>
                </a>
                <a className="carousel-control-next" href="#carousel-example-1z" role="button" data-slide="next">
                <span className="carousel-control-next-icon" aria-hidden="true" />
                <span className="sr-only">Next</span>
                </a>
                {/*/.Controls*/}
            </div>
        );
    }
}

export default Wrapper;