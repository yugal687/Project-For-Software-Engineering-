"use client";
import React, { useState, useEffect } from "react";
import { useRouter, usePathname, useParams } from "next/navigation";
import Dashboard from "@/components/studentComponents/DashboardLayout";
import axios from "axios";
// import Image from "next/image";

const page = () => {
  const [data, setData] = useState("");
  const [dataStudent, setStudentData] = useState({});

  const [error, setError] = useState(null);
  const router = useRouter();
  // const id = localStorage.getItem("user_id");
  // const params = useParams();
  // const token = params.token;
  // const { id } = router.query.id;
  // const id = localStorage.getItem("user_id");

  // Fetch CSRF token
  // async function getCSRFToken() {
  //   const response = await fetch("http://127.0.0.1:8000/api/student/csrf/", {
  //     credentials: "include", // Include cookies in requests
  //   });
  //   const data = await response.json();
  //   console.log("CSRF Token:", document.cookie); // Verify cookie
  // }

  // async function makeAuthenticatedRequest() {
  //   const response = await axios.get(
  //     `http://127.0.0.1:8000/api/student/${get_id}`
  //   );
  //   // const data = await response.json();
  //   setStudentData(response.data);
  //   // console.log("Dashboard Data:", data);
  // }
  // async function get_all_opportunities() {
  //   const response = await axios.get(
  //     "http://127.0.0.1:8000/api/student/get-active-opportunities"
  //   );
  //   setData(response.data);
  // }

  useEffect(() => {
    // makeAuthenticatedRequest();
    // get_all_opportunities();
    const token = localStorage.getItem("access-token");
    const id = localStorage.getItem("user_id");

    const fetchData = async () => {
      // setIsLoading(true);
      console.log(id);
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/student/${id}/`
          // {
          //   headers: { Authorization: `Token ${token}` }, // Forward the authorization header
          // }
        );
        console.log(response);
        // const data = await response.json();

        setStudentData(response.data);
      } catch (error) {
        setError(error);
      } finally {
        // setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Dashboard>
        {/* Profile Information */}
        <div className="pt-1 pb-2 mb-3 border-bottom px-2">
          Student Dashboard
        </div>
        <section className="mb-4">
          <h4>Profile Information:</h4>
          <div className="card p-3 mb-4">
            <div className="row">
              <div className="col-md-6">
                <div>
                  {/* <Image
                    src={data && data.profile_picture}
                    width="200"
                    height="200"
                  /> */}
                </div>
                <p>
                  <strong>Name: </strong>
                  {dataStudent.full_name}
                </p>
                <p>
                  <strong>Email:</strong> {dataStudent.email}
                </p>
                <p>
                  <strong>Major:</strong> {dataStudent.major}
                </p>
                <p>
                  <strong>Graduation Year:</strong>{" "}
                  {dataStudent.graduation_year}
                </p>
                <p>
                  <strong>Certification:</strong> {dataStudent.certification}
                </p>
                <p>
                  <strong>Skills:</strong> {dataStudent.skills}
                </p>
              </div>
              <div className="col-md-6">
                <p>
                  <strong>Year:</strong> {dataStudent.year}
                </p>
                <p>
                  <strong>University:</strong> University of North Texas
                </p>
                <p>
                  <strong>GPA:</strong> {dataStudent.gpa}
                </p>
                <p>
                  <strong>LinkedIn:</strong> {dataStudent.linked_in_profile}
                </p>
                <p>
                  <strong>Github:</strong> {dataStudent.github_profile}
                </p>
                <p>
                  <strong>Protfolio Website:</strong>{" "}
                  {dataStudent.portfolio_website}
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
