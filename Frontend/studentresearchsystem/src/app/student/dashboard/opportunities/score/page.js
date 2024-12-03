import React from "react";
import { Flex, Progress } from "antd";
import StudentDashboard from "@/components/studentComponents/DashboardLayout";

const page = () => (
  <StudentDashboard>
    <Flex
      gap="small"
      wrap
      style={{
        width: 400,
      }}
    >
      <Progress size={300} type="dashboard" percent={75} />
    </Flex>
    <div>Your Resume matching score with Score is 75%</div>
  </StudentDashboard>
);
export default page;
