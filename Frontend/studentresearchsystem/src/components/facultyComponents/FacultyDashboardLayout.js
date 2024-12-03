"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter, usePathname, useParams } from "next/navigation";
import axios from "axios";
import Image from "next/image";
import logo from "@/assets/unt-logo.png";

const FacultyDashboardLayout = ({ children }) => {
  const [data, setData] = useState("");
  const [error, setError] = useState(null);
  const router = useRouter();
  const params = useParams();
  const pathname = usePathname();

  // const token = params.token;
  // const { id } = router.query.id;
  // const id = localStorage.getItem("user_id");
  const token = localStorage.getItem("access-token");
  const id = localStorage.getItem("user_id");
  //

  const handleLogout = () => {
    // localStorage.removeItem("accessToken");
    // localStorage.removeItem("refreshToken");
    router.push("/faculty/login");
  };

  useEffect(() => {
    // if (!token) {
    //   return router.push("/faculty/login");
    // }
    // setIsLoading(true);

    const fetchData = async () => {
      // try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/professor/${id}/`,
        {
          headers: { Authorization: `Token ${token}` }, // Forward the authorization header
        }
      );
      const data = await response.json();
      console.log(data);
      setData(data);
      // } catch (error) {
      //   setError(error);
      // } finally {
      //   // setIsLoading(false);
      // }
    };

    fetchData();
  }, [token]);

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
                      pathname === "/faculty/dashboard"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/faculty/dashboard"
                >
                  <i className="bi bi-house-door"></i> Dashboard
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/faculty/dashboard/profile"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/faculty/dashboard/profile"
                >
                  <i className="bi bi-person"></i> Profile
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/faculty/dashboard/student-applications"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/faculty/dashboard/student-applications"
                >
                  <i className="bi bi-file-earmark-arrow-up"></i> View
                  Applicants
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className={
                    "nav-link " +
                    `${
                      pathname === "/faculty/dashboard/opportunities"
                        ? "active"
                        : "text-white"
                    }`
                  }
                  href="/faculty/dashboard/opportunities"
                >
                  <i className="bi bi-person"></i> View My Research Posts
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
          <nav class="navbar navbar-light primary-background p-3 dash-nav">
            <div class="d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between">
              <a class="navbar-brand text-white fw-bold" href="#">
                Faculty Dashboard
              </a>
              <button
                class="navbar-toggler d-md-none collapsed mb-3"
                type="button"
                data-toggle="collapse"
                data-target="#sidebar"
                aria-controls="sidebar"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span class="navbar-toggler-icon"></span>
              </button>
            </div>
            <div class="col-12 col-md-4 col-lg-2">
              <input
                class="form-control form-control-dark"
                type="text"
                placeholder="Search"
                aria-label="Search"
              />
            </div>
            <div class="col-12 col-md-5 col-lg-8 d-flex align-items-center justify-content-md-end mt-3 mt-md-0">
              <div class="dropdown">
                <button
                  class="btn bg-white primary-color dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Hello {data.first_name} {data.last_name}
                </button>
                <ul class="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="#">
                      Profile
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#"></a>
                  </li>
                  <li>
                    <a
                      onClick={handleLogout}
                      className="dropdown-item"
                      href="#"
                    >
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

export default FacultyDashboardLayout;
