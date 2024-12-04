"use client";
import React from "react";
import { Flex, Progress } from "antd";
import StudentDashboard from "@/components/studentComponents/DashboardLayout";

const page = () => {
  const score = localStorage.getItem("user_score");
  return (
    <StudentDashboard>
      <Flex gap="small" wrap>
        <Progress size={400} type="dashboard" percent={score} />
      </Flex>
      <div>Your Resume matching score with Score is {score}</div>
    </StudentDashboard>
  );
};
export default page;
