// components/ResearchOpportunityForm.js
"use client";
import React, { useState } from "react";

const ResearchOpportunityForm = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [eligibility, setEligibility] = useState("");
  const [deadline, setDeadline] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Handle form submission (e.g., send data to your API)
    const formData = {
      title,
      description,
      eligibility,
      deadline,
    };

    console.log("Form submitted:", formData);
    // You can send this data to your backend or API here
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <div className="mb-3">
        <label htmlFor="title" className="form-label">
          Title
        </label>
        <input
          type="text"
          className="form-control"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="description" className="form-label">
          Description
        </label>
        <textarea
          className="form-control"
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        ></textarea>
      </div>
      <div className="mb-3">
        <label htmlFor="eligibility" className="form-label">
          Eligibility Criteria
        </label>
        <input
          type="text"
          className="form-control"
          id="eligibility"
          value={eligibility}
          onChange={(e) => setEligibility(e.target.value)}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="deadline" className="form-label">
          Application Deadline
        </label>
        <input
          type="date"
          className="form-control"
          id="deadline"
          value={deadline}
          onChange={(e) => setDeadline(e.target.value)}
          required
        />
      </div>
      <button type="submit" className="btn btn-primary">
        Create Research Opportunity
      </button>
    </form>
  );
};

export default ResearchOpportunityForm;
