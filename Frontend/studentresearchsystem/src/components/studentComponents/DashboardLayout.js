"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter, usePathname, useParams } from "next/navigation";
import axios from "axios";
import Image from "next/image";
import logo from "@/assets/unt-logo.png";

const StudentDashboard = ({ children }) => {
  // const [data, setData] = useState("");
  const [error, setError] = useState(null);
  const router = useRouter();
  const params = useParams();
  const pathname = usePathname();

  // useEffect(() => {
  // if (!token) {
  //   return router.push("/faculty/login");
  // }
  // setIsLoading(true);

  //   const fetchData = async () => {
  //     try {
  //       // const response = await fetch(
  //       //   `http://127.0.0.1:8000/api/student/dashboard/`,
  //       //   {
  //       //     withCredentials: true, // Include cookies in requests
  //       //   }
  //       // );
  //       const response = await axios.get(
  //         "http://127.0.0.1:8000/api/student/dashboard/",
  //         {
  //           withCredentials: true, // Include cookies in requests
  //         }
  //       );

  //       // return response.data; // Dashboard data
  //       const data = await response.json();
  //       console.log(data);
  //       setData(data);
  //     } catch (error) {
  //       setError(error);
  //     } finally {
  //       // setIsLoading(false);
  //     }
  //   };

  //   fetchData();
  // }, [router]);

  // // useEffect(() => {
  //   async function fetchData() {
  //     try {
  //       const dashboardData = await fetchStudentDashboard();
  //       setData(dashboardData);
  //     } catch (err) {
  //       setError(err.error || "Failed to load dashboard");
  //     }
  //   }
  //   fetchData();
  // }, []);

  return (
    <div className="container-fluid">
      <div className="row">
        <nav className="col-md-2 d-none d-md-block primary-background sidebar">
          <div className="position-sticky pt-3">
            {" "}
            {/* <img width="100" className="sidebar-logo img-fluid" src={logo} /> */}
            <Image src={logo} alt="Landscape picture" width={100} />
            <ul className="nav flex-column mt-3">
              <li className="nav-item">
                {" "}
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/student/dashboard"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/student/dashboard"
                >
                  <i className="bi bi-house-door"></i> Dashboard
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/student/dashboard/profile"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/student/dashboard/profile"
                >
                  <i className="bi bi-person"></i> Profile
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/student/dashboard/opportunities"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/student/dashboard/opportunities"
                >
                  <i className="bi bi-file-earmark-arrow-up"></i> View
                  Opportunities
                </Link>
              </li>

              <li className="nav-item">
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/faculty/dashboard/settings"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="#"
                >
                  <i className="bi bi-gear"></i> Settings
                </Link>
              </li>
            </ul>
          </div>
        </nav>

        {/* Main content area */}
        <main className="col-md-9 ms-sm-auto col-lg-10 px-0">
          <nav className="navbar navbar-light primary-background p-3 dash-nav">
            <div className="d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between">
              <a className="navbar-brand text-white fw-bold" href="#">
                Student Dashboard
              </a>
              <button
                className="navbar-toggler d-md-none collapsed mb-3"
                type="button"
                data-toggle="collapse"
                data-target="#sidebar"
                aria-controls="sidebar"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span className="navbar-toggler-icon"></span>
              </button>
            </div>
            <div className="col-12 col-md-4 col-lg-2">
              <input
                className="form-control form-control-dark"
                type="text"
                placeholder="Search"
                aria-label="Search"
              />
            </div>
            <div className="col-12 col-md-5 col-lg-8 d-flex align-items-center justify-content-md-end mt-3 mt-md-0">
              <div className="dropdown">
                <button
                  className="btn bg-white primary-color dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Hello
                  {/* {data.first_name} {data.last_name} */}
                </button>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="#">
                      Profile
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#"></a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Logout
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </nav>

          <div className="pt-3 pb-2 mb-3 border-bottom px-3">{children}</div>
        </main>
      </div>
    </div>
  );
};

export default StudentDashboard;
