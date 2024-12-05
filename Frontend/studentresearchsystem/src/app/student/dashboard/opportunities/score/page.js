"use client";
import React from "react";
import { Flex, Progress } from "antd";
import StudentDashboard from "@/components/studentComponents/DashboardLayout";

const page = () => {
  const score = localStorage.getItem("user_score");
  return (
    <StudentDashboard>
      <div className="row py-5">
        <div className="col-md-12 text-center">
          <Flex gap="small" wrap>
            <Progress size={400} type="dashboard" percent={72.8} />
          </Flex>
        </div>
        <div className="">
          <h5 className="fw-bold">Recommended Skills:</h5>
          <div>Deep Learning, CNN, RNN, LLMs, AWS, MLOPS, DEVOPS.</div>
        </div>
      </div>

      <div>Your Resume matching score with opportunity is 72.8%</div>
    </StudentDashboard>
  );
};
export default page;
