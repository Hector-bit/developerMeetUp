import React, { Component } from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import HomepageTop from './HomepageTop';
import { render } from 'react-dom'

export default class App extends Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div id="container">
                <BrowserRouter>
                    <HomepageTop/>
                </BrowserRouter>
            </div>
        )
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv)