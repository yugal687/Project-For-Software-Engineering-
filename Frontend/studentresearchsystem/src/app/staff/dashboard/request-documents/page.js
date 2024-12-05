import DashboardLayout from "@/components/staffComponents/StaffDashboardLayout";
import React from "react";

const page = () => {
  return (
    <div>
      <DashboardLayout>
        <div className="card p-4 documentation">
          <h5>Students who are accepted</h5>
          <ul>
            <li className="py-3">
              Bilkul Sharma{" "}
              <button className="btn btn-success">Request Documents</button>
            </li>
            <li className="py-3">
              Max Gp{" "}
              <button className="btn btn-success">Request Documents</button>
            </li>
            <li className="py-3">
              Binod Sharma{" "}
              <button className="btn btn-success" disabled>
                Requested Already
              </button>
            </li>
            <li className="py-3">
              Jyothi Sharma{" "}
              <button className="btn btn-success">Request Documents</button>
            </li>
          </ul>
        </div>
      </DashboardLayout>
    </div>
  );
};

export default page;
