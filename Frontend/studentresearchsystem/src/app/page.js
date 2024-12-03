"use client";
import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Link from "next/link";
import Navbar from "@/components/Navbar";

// export async function getServerSideProps() {
//   const res = await fetch("http://localhost:8000/api/professor/");
//   const data = await res.json();

//   return { props: { data } };
// }

const Home = async () => {
  // const [data, setData] = useState([]);
  // const [loading, setLoading] = useState(true);
  // const res = await fetch("http://localhost:8000/api/professor/");
  // const data = await res.json();

  // useEffect(() => {
  //   const fetchData = async () => {
  //     const response = await fetch("http://localhost:8000/api/professor/");
  //     const result = await response.json();
  //     setData(result);
  //     setLoading(false);
  //   };
  //   console.log(data);
  //   fetchData();
  // }, []);
  return (
    <div className="landing-page">
      {/* Navigation */}
      {/* <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <a className="navbar-brand" href="#">
            Student Research Hub
          </a>

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
      </nav> */}
      <Navbar />

      {/* Hero Section */}
      <div className="primary-background text-white text-center py-5">
        <div className="container">
          <h1 className="display-4">Discover Student Research Opportunities</h1>
          <p className="lead">
            Find, explore, and engage with research projects that match your
            interests.
          </p>

          {/* Search Bar */}
          <div className="input-group mb-3 w-50 mx-auto">
            <input
              type="text"
              className="form-control"
              placeholder="Search research opportunities..."
            />
            <button className="btn btn-primary" type="button">
              Search
            </button>
          </div>
        </div>
      </div>

      {/* Benefits Section */}
      <section id="about" className="py-5">
        <div className="container">
          <h3 className="text-center mb-4">Why Join Student Research?</h3>
          <div className="row">
            <div className="col-md-3 text-center">
              <i
                className="bi bi-bookmark-fill mb-3"
                style={{ fontSize: "2rem" }}
              ></i>
              <p>Expand your knowledge beyond the classroom.</p>
            </div>
            <div className="col-md-3 text-center">
              <i
                className="bi bi-laptop-fill mb-3"
                style={{ fontSize: "2rem" }}
              ></i>
              <p>Gain hands-on experience in real-world research.</p>
            </div>
            <div className="col-md-3 text-center">
              <i
                className="bi bi-people-fill mb-3"
                style={{ fontSize: "2rem" }}
              ></i>
              <p>Connect with mentors and professionals in your field.</p>
            </div>
            <div className="col-md-3 text-center">
              <i
                className="bi bi-award-fill mb-3"
                style={{ fontSize: "2rem" }}
              ></i>
              <p>Boost your resume for future job or academic applications.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Projects Section */}
      <section id="featured" className="primary-background text-white  py-5">
        <div className="container">
          <h3 className="text-center mb-4">Featured Research Projects</h3>
          <div className="row">
            <div className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">AI in Healthcare</h5>
                  <p className="card-text">
                    Explore how artificial intelligence is revolutionizing the
                    healthcare industry.
                  </p>
                  <a href="#" className="btn btn-outline-primary">
                    Learn More
                  </a>
                </div>
              </div>
            </div>
            <div className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">Climate Change Research</h5>
                  <p className="card-text">
                    Join a team studying the effects of climate change on
                    biodiversity.
                  </p>
                  <a href="#" className="btn btn-outline-primary">
                    Learn More
                  </a>
                </div>
              </div>
            </div>
            <div className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">Quantum Computing</h5>
                  <p className="card-text">
                    Get involved in cutting-edge research on the future of
                    computing.
                  </p>
                  <a href="#" className="btn btn-outline-primary">
                    Learn More
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Call to Action */}
      <section id="contact" className="py-5 text-center">
        <div className="container">
          <h3>Ready to Start Your Research Journey?</h3>
          <p>
            Sign up today and start exploring research opportunities that match
            your academic goals.
          </p>
          <button className="btn btn-primary btn-lg">Get Started</button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-dark text-white py-4">
        <div className="container text-center">
          <p>&copy; 2024 Student Research Hub. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Home;
