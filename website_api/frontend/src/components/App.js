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
                {/* <BrowserRouter>
                    <Link to='/'>Home</Link>
                    <Link>Log in</Link>
                    <Link>Sign up</Link>
                    <Routes>
                        <Route path='/' element={<HomepageTop/>}></Route>
                    </Routes>
                </BrowserRouter> */}
                <h2>heool there</h2>
                <HomepageTop/>
            </div>
        )
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv)