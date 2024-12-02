"use client";
import React, { useState, useEffect } from "react";
import { useRouter, usePathname, useParams } from "next/navigation";
import Dashboard from "@/components/studentComponents/DashboardLayout";
import axios from "axios";

const page = () => {
  const [data, setData] = useState("");
  const [error, setError] = useState(null);
  const router = useRouter();
  // const params = useParams();
  // const token = params.token;
  // const { id } = router.query.id;
  // const id = localStorage.getItem("user_id");

  // Fetch CSRF token
  async function getCSRFToken() {
    const response = await fetch("http://127.0.0.1:8000/api/student/csrf/", {
      credentials: "include", // Include cookies in requests
    });
    const data = await response.json();
    console.log("CSRF Token:", document.cookie); // Verify cookie
  }

  async function makeAuthenticatedRequest() {
    const csrfToken = document.cookie.split("csrftoken=")[1];
    const response = await fetch(
      "http://127.0.0.1:8000/api/student/dashboard/",
      {
        method: "GET",
        credentials: "include", // Include session cookies
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken, // Extract CSRF token from cookies
        },
      }
    );
    const data = await response.json();
    console.log("Dashboard Data:", data);
  }

  useEffect(() => {
    getCSRFToken();
    makeAuthenticatedRequest();
    // const fetchData = async () => {
    //   const response = await axios.get(
    //     "http://127.0.0.1:8000/api/student/dashboard",
    //     // {
    //     //   headers: "Access-Control-Allow-Origin",
    //     // }
    //     { withCredentials: true }
    //   );
    //   const data = await response.data;
    //   console.log(data);
    //   setData(data);
    // };

    // fetchData();
  }, []);

  return (
    <div>
      <Dashboard data={data}>
        {/* Profile Information */}
        <div className="pt-1 pb-2 mb-3 border-bottom px-2">
          Student Dashboard
        </div>
        <section className="mb-4">
          <h4>Profile Information</h4>
          <div className="card p-3 mb-4">
            <div className="row">
              <div className="col-md-6">
                <p>
                  <strong>Name:</strong>
                </p>
                <p>
                  <strong>Email:</strong> johndoe@example.com
                </p>
                <p>
                  <strong>Major:</strong> Computer Science
                </p>
              </div>
              <div className="col-md-6">
                <p>
                  <strong>Year:</strong> Senior
                </p>
                <p>
                  <strong>University:</strong> University of North Texas
                </p>
                <p>
                  <strong>GPA:</strong> 3.8
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Resume Upload */}
        <section className="mb-4">
          <h4>Upload Your Resume</h4>
          <div className="card p-3">
            <form>
              <div className="mb-3">
                <label htmlFor="resumeUpload" className="form-label">
                  Select resume file (PDF or DOCX):
                </label>
                <input
                  className="form-control"
                  type="file"
                  id="resumeUpload"
                  accept=".pdf,.doc,.docx"
                />
              </div>
              <button type="submit" className="btn btn-primary">
                Upload Resume
              </button>
            </form>
          </div>
        </section>
      </Dashboard>
    </div>
  );
};

export default page;
