import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const Dashboard = () => {
  return (
    <div className="d-flex">
      {/* Sidebar */}
      <nav className="col-md-2 d-none d-md-block bg-light sidebar">
        <div className="position-sticky pt-3">
          <ul className="nav flex-column">
            <li className="nav-item">
              <a className="nav-link active" href="#">
                <i className="bi bi-house-door"></i> Dashboard
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                <i className="bi bi-person"></i> Profile
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                <i className="bi bi-file-earmark-arrow-up"></i> Upload Resume
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                <i className="bi bi-gear"></i> Settings
              </a>
            </li>
          </ul>
        </div>
      </nav>

      {/* Main Content */}
      <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
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
                  <strong>Name:</strong> John Doe
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
                  <strong>University:</strong> University of ABC
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
      </main>
    </div>
  );
};

export default Dashboard;
