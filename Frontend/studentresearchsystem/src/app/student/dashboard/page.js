import React from "react";
import Dashboard from "@/components/DashboardLayout";

const page = () => {
  return (
    <div>
      <Dashboard>
        <div className="pt-3 pb-2 mb-3 border-bottom">
          <h2>Student Dashboard</h2>
        </div>

        {/* Profile Information */}
        <section className="mb-4">
          <h4>Profile Information</h4>
          <div className="card p-3 mb-4">
            <div className="row">
              <div className="col-md-6">
                <p>
                  <strong>Name:</strong> James Bond
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
