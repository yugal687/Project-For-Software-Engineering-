import DashboardLayout from "@/components/staffComponents/StaffDashboardLayout";
import React from "react";

const page = () => {
  return (
    <div>
      <DashboardLayout>
        <div className="card p-4 documentation">
          <h5>Students who are accepted</h5>
          <div className="row">
            <div className="col-md-4">
              <div className="card p-4 m-2">
                <p className="fw-bold">Topic :</p>
                <p>
                  VR lab tool Training hands-on experience with labs tools and
                  software
                </p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card p-4 m-2">
                <p className="fw-bold">Topic :</p>
                <p>Compliance Training Bridge Training</p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card p-4 m-2">
                <p className="fw-bold">Topic :</p>
                <p>
                  Soft Skills and Personal Development Resource training on
                  effective communication, time management, and interpersonal
                  skills.
                </p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card p-4 m-2">
                <p className="fw-bold">Topic :</p>
                <p>
                  VR lab tool Training hands-on experience with labs tools and
                  software
                </p>
              </div>
            </div>
          </div>
        </div>
      </DashboardLayout>
    </div>
  );
};

export default page;
