"use client";
import React, { useState, useEffect } from "react";
import Dashboard from "@/components/facultyComponents/Dashboard";

const page = () => {
  const [data, setData] = useState("");
  const [error, setError] = useState(null);
  // const router = useRouter();
  // const params = useParams();
  // const token = params.token;
  // const { id } = router.query.id;
  // const id = localStorage.getItem("user_id");

  useEffect(() => {
    const fetchData = async () => {
      // setIsLoading(true);
      const token = localStorage.getItem("access-token");
      const id = localStorage.getItem("user_id");

      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/professor/${id}/`,
          {
            headers: { Authorization: `Token ${token}` }, // Forward the authorization header
          }
        );
        const data = await response.json();
        console.log(data);
        setData(data);
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
      <Dashboard data={data}>
        {/* Profile Information */}
        <div className="pt-1 pb-2 mb-3 border-bottom px-2">
          Faculty Dashboard
        </div>
        <section className="mb-4">
          <h4>Profile Information</h4>
          <div className="card p-3 mb-4">
            <div className="row">
              <div className="col-md-6">
                <p>
                  <strong>Name:</strong> {data.first_name}
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
