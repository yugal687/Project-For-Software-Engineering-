import ResearchOpportunityForm from "@/components/facultyComponents/CreateResearchOpportunityForm";
import FacultyDashboard from "@/components/facultyComponents/FacultyDashboardLayout";
import React from "react";

const page = () => {
  return (
    <div>
      <FacultyDashboard>
        <ResearchOpportunityForm />
      </FacultyDashboard>
    </div>
  );
};

export default page;
