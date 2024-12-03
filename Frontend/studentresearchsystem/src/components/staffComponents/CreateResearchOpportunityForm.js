"use client";
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const CreateResearchOpportunityForm = () => {
  // State to manage form values
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    deadline: "",
    isActive: false,
    skills: "",
    tags: "",
    maxApplications: "",
    currentApplications: "",
    professor: "",
  });

  // Handle form field changes
  const handleChange = (e) => {
    const { id, value, type, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [id]: type === "checkbox" ? checked : value,
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/professor/opportunity/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      if (response.ok) {
        alert("Form submitted successfully");
        setFormData({
          title: "",
          description: "",
          deadline: "",
          isActive: false,
          skills: "",
          tags: "",
          maxApplications: "",
          currentApplications: "",
          professor: "",
        });
      } else {
        alert("Failed to submit form");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error submitting form");
    }
  };

  return (
    <div className="container mt-5">
      <h2>Create a New Application</h2>
      <form onSubmit={handleSubmit}>
        {/* Title Field */}
        <div className="mb-3">
          <label htmlFor="title" className="form-label">
            Title
          </label>
          <input
            type="text"
            className="form-control"
            id="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="Enter title"
            required
          />
        </div>

        {/* Description Field */}
        <div className="mb-3">
          <label htmlFor="description" className="form-label">
            Description
          </label>
          <textarea
            className="form-control"
            id="description"
            rows="3"
            value={formData.description}
            onChange={handleChange}
            placeholder="Enter description"
            required
          ></textarea>
        </div>

        {/* Deadline Field */}
        <div className="mb-3">
          <label htmlFor="deadline" className="form-label">
            Deadline
          </label>
          <input
            type="datetime-local"
            className="form-control"
            id="deadline"
            value={formData.deadline}
            onChange={handleChange}
            required
          />
        </div>

        {/* Is Active Checkbox */}
        <div className="mb-3 form-check">
          <input
            type="checkbox"
            className="form-check-input"
            id="isActive"
            checked={formData.isActive}
            onChange={handleChange}
          />
          <label className="form-check-label" htmlFor="isActive">
            Is Active
          </label>
        </div>

        {/* Required Skills Field */}
        <div className="mb-3">
          <label htmlFor="skills" className="form-label">
            Required Skills
          </label>
          <input
            type="text"
            className="form-control"
            id="skills"
            value={formData.skills}
            onChange={handleChange}
            placeholder="Enter required skills"
          />
        </div>

        {/* Research Tags Field */}
        <div className="mb-3">
          <label htmlFor="tags" className="form-label">
            Research Tags
          </label>
          <input
            type="text"
            className="form-control"
            id="tags"
            value={formData.tags}
            onChange={handleChange}
            placeholder="Enter research tags"
          />
        </div>

        {/* Max Applications Field */}
        <div className="mb-3">
          <label htmlFor="maxApplications" className="form-label">
            Max Applications
          </label>
          <input
            type="number"
            className="form-control"
            id="maxApplications"
            value={formData.maxApplications}
            onChange={handleChange}
            placeholder="Enter max applications"
            required
          />
        </div>

        {/* Current Applications Field */}
        <div className="mb-3">
          <label htmlFor="currentApplications" className="form-label">
            Current Applications
          </label>
          <input
            type="number"
            className="form-control"
            id="currentApplications"
            value={formData.currentApplications}
            onChange={handleChange}
            placeholder="Enter current applications"
            required
          />
        </div>

        {/* Professor Field */}
        <div className="mb-3">
          <label htmlFor="professor" className="form-label">
            Professor
          </label>
          <input
            type="text"
            className="form-control"
            id="professor"
            value={formData.professor}
            onChange={handleChange}
            placeholder="Enter professor name"
            required
          />
        </div>

        {/* Submit Button */}
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
  );
};

export default CreateResearchOpportunityForm;
