import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Logo from "./logo.png";
import "./navbar.css";

const MyNavbar = () => {
  return (
    <div>
      <Navbar
        fixed="top"
        variant="dark"
        expand ="md"
        className="animate-navbar nav-theme justify-content-between"
      >
        <div>
         <Navbar.Brand href="#home">
            <img className="logo" src={Logo} alt="" />
          </Navbar.Brand>
        </div>
        <div>
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="#home"> Home </Nav.Link>
              <Nav.Link href="#login"> Login </Nav.Link>
              <Nav.Link href="#signup"> Signup </Nav.Link>

            </Nav>
          </Navbar.Collapse>
        </div>
      </Navbar>
    </div>
  );
};

export default MyNavbar;