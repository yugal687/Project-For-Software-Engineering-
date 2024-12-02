import React from "react";
import LoginPage from "@/components/studentComponents/StudentLogin";

function page({ Loginfor }) {
  return (
    <div>
      <LoginPage Loginfor={"Student"} />
    </div>
  );
}

export default page;
