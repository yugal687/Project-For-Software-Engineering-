import React from "react";
import Dashboard from "@/components/DashboardLayout";

const profile = () => {
  return (
    <Dashboard>
      <div>
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
      </div>
    </Dashboard>
  );
};

export default profile;
