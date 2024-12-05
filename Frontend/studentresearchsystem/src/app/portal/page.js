// import "bootstrap/dist/css/bootstrap.min.css";
"use client";
import Link from "next/link";
import React, { useState } from "react";

const PortalPage = () => {
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <Link className="navbar-brand" href="/">
            Student Research Hub
          </Link>

          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link" href="#about">
                  About
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#opportunities">
                  Opportunities
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#featured">
                  Featured Projects
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#contact">
                  Contact
                </a>
              </li>
              <li className="nav-item">
                <Link className="nav-link" href="/portal">
                  Portals
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" href="/faculty/login">
                  Login
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container-fluid primary-background">
        <div className="container py-5">
          <h2 className="text-center text-white mb-4">
            Welcome to the Login Portal
          </h2>
          <div className="row justify-content-center">
            {/* Student Portal */}
            <div className="col-md-4 mb-4">
              <div className="card shadow-sm border-primary">
                <div className="card-body text-center">
                  <h4 className="card-title text-primary">
                    Are you a Student?
                  </h4>
                  <p className="card-text">
                    Login to your student portal to access resources and grades.
                  </p>
                  <Link href="/student/login">
                    <button className="btn btn-primary w-100">
                      Click Here
                    </button>
                  </Link>
                </div>
              </div>
            </div>

            {/* Professor Portal */}
            <div className="col-md-4 mb-4">
              <div className="card shadow-sm border-success">
                <div className="card-body text-center">
                  <h4 className="card-title text-success">
                    Are you a Professor?
                  </h4>
                  <p className="card-text">
                    Login to your professor portal to manage courses and grades.
                  </p>
                  <Link href="/faculty/login">
                    <button className="btn btn-success w-100">
                      Click Here
                    </button>
                  </Link>
                </div>
              </div>
            </div>

            {/* Staff Portal */}
            <div className="col-md-4 mb-4">
              <div className="card shadow-sm border-warning">
                <div className="card-body text-center">
                  <h4 className="card-title text-warning">
                    Are you a Staff Member?
                  </h4>
                  <p className="card-text">
                    Login to the staff portal to manage administrative tasks.
                  </p>
                  <Link href="/staff/login">
                    <button className="btn btn-warning w-100">
                      Click Here
                    </button>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default PortalPage;
