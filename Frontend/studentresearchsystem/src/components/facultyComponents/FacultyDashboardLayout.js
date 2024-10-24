// import React from "react";
// import "bootstrap/dist/css/bootstrap.min.css";

// const Dashboard = () => {
//   return (
//     <div className="d-flex">
//       {/* Sidebar */}
//       <nav className="col-md-2 d-none d-md-block bg-light sidebar">
//         <div className="position-sticky pt-3">
//           <ul className="nav flex-column">
//             <li className="nav-item">
//               <a className="nav-link active" href="#">
//                 <i className="bi bi-house-door"></i> Dashboard
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="#">
//                 <i className="bi bi-person"></i> Profile
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="#">
//                 <i className="bi bi-file-earmark-arrow-up"></i> Upload Resume
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="#">
//                 <i className="bi bi-person"></i> Research Searches
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="#">
//                 <i className="bi bi-person"></i> Opportunities Searches
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="#">
//                 <i className="bi bi-gear"></i> Settings
//               </a>
//             </li>
//           </ul>
//         </div>
//       </nav>

//       {/* Main Content */}
//       <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
//         <div className="pt-3 pb-2 mb-3 border-bottom">
//           <h2>Student Dashboard</h2>
//         </div>

//         {/* Profile Information */}
//         <section className="mb-4">
//           <h4>Profile Information</h4>
//           <div className="card p-3 mb-4">
//             <div className="row">
//               <div className="col-md-6">
//                 <p>
//                   <strong>Name:</strong> James Bond
//                 </p>
//                 <p>
//                   <strong>Email:</strong> johndoe@example.com
//                 </p>
//                 <p>
//                   <strong>Major:</strong> Computer Science
//                 </p>
//               </div>
//               <div className="col-md-6">
//                 <p>
//                   <strong>Year:</strong> Senior
//                 </p>
//                 <p>
//                   <strong>University:</strong> University of North Texas
//                 </p>
//                 <p>
//                   <strong>GPA:</strong> 3.8
//                 </p>
//               </div>
//             </div>
//           </div>
//         </section>

//         {/* Resume Upload */}
//         <section className="mb-4">
//           <h4>Upload Your Resume</h4>
//           <div className="card p-3">
//             <form>
//               <div className="mb-3">
//                 <label htmlFor="resumeUpload" className="form-label">
//                   Select resume file (PDF or DOCX):
//                 </label>
//                 <input
//                   className="form-control"
//                   type="file"
//                   id="resumeUpload"
//                   accept=".pdf,.doc,.docx"
//                 />
//               </div>
//               <button type="submit" className="btn btn-primary">
//                 Upload Resume
//               </button>
//             </form>
//           </div>
//         </section>
//       </main>
//     </div>
//   );
// };

// export default Dashboard;

import React from "react";
import Link from "next/link";

const FacultyDashboard = ({ children }) => {
  return (
    <div className="container-fluid">
      <div className="row">
        <nav className="col-md-2 d-none d-md-block bg-light sidebar">
          <div className="position-sticky pt-3">
            {" "}
            <ul className="nav flex-column">
              <li className="nav-item">
                {" "}
                <Link className="nav-link active" href="/faculty/dashboard">
                  <i className="bi bi-house-door"></i> Dashboard
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" href="/faculty/dashboard/profile">
                  <i className="bi bi-person"></i> Profile
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" href="#">
                  <i className="bi bi-file-earmark-arrow-up"></i> View
                  Applicants
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className="nav-link"
                  href="/student/dashboard/research-projects"
                >
                  <i className="bi bi-person"></i> View My Research Posts
                </Link>
              </li>

              <li className="nav-item">
                <Link className="nav-link" href="#">
                  <i className="bi bi-gear"></i> Settings
                </Link>
              </li>
            </ul>
          </div>
        </nav>

        {/* Main content area */}
        <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <nav class="navbar navbar-light bg-light p-3">
            <div class="d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between">
              <a class="navbar-brand" href="#">
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
              <div class="mr-3 mt-1">
                <a
                  class="github-button"
                  href="https://github.com/themesberg/simple-bootstrap-5-dashboard"
                  data-color-scheme="no-preference: dark; light: light; dark: light;"
                  data-icon="octicon-star"
                  data-size="large"
                  data-show-count="true"
                  aria-label="Star /themesberg/simple-bootstrap-5-dashboard"
                >
                  Star
                </a>
              </div>
              <div class="dropdown">
                <button
                  class="btn btn-secondary dropdown-toggle"
                  type="button"
                  id="dropdownMenuButton"
                  data-toggle="dropdown"
                  aria-expanded="false"
                >
                  Hello, John Doe
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                  <li>
                    <a class="dropdown-item" href="#">
                      Settings
                    </a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">
                      Messages
                    </a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">
                      Sign out
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </nav>
          <div className="pt-3 pb-2 mb-3 border-bottom">
            <h1 className="h2">Dashboard</h1>
          </div>
          {children}
        </main>
      </div>
    </div>
  );
};

export default FacultyDashboard;
