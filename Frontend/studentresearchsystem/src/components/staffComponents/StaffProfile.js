import React from "react";
import Dashboard from "@/components/facultyComponents/FacultyDashboardLayout";

const FacultyProfile = () => {
  return (
    <div>
      <Dashboard>
        <div>
          <div className="pt-1 pb-2 mb-3 border-bottom px-2">
            Faculty Profile
          </div>
          <section className="mb-4">
            <h4>Profile Information</h4>
            <div className="card p-3 mb-4">
              <div className="row">
                <div className="col-md-6">
                  <p>
                    <strong>Name:</strong> Sharad Sharma
                  </p>
                  <p>
                    <strong>Email:</strong> sharmaSd@example.com
                  </p>
                  <p>
                    <strong>Department:</strong> Computer Science
                  </p>
                </div>
                <div className="col-md-6">
                  <p>
                    <strong>University:</strong> University of North Texas
                  </p>
                </div>
              </div>
            </div>
          </section>
        </div>
      </Dashboard>
    </div>
  );
};

export default FacultyProfile;
