import React, { useState } from "react";
import axios from "axios";

const CreateResearchOpportunity = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [deadline, setDeadline] = useState("");
  const [maxApplications, setMaxApplications] = useState(10);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newOpportunity = {
      title,
      description,
      deadline,
      max_applications: maxApplications,
    };

    // Get the stored token
    const token = localStorage.getItem('access_token');

    try {
      const response = await axios.post(
        "http://localhost:8000/professor/api/researchopportunities/",
        newOpportunity,
        {
          headers: {
            'Authorization': `Bearer ${token}`, // Include the JWT token
          },
        }
      );
      console.log("Research Opportunity created:", response.data);
    } catch (error) {
      console.error("Error creating research opportunity:", error);
    }
  };

  return (
    <div>
      <h2>Create Research Opportunity</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Description:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <div>
          <label>Deadline:</label>
          <input
            type="date"
            value={deadline}
            onChange={(e) => setDeadline(e.target.value)}
          />
        </div>
        <div>
          <label>Max Applications:</label>
          <input
            type="number"
            value={maxApplications}
            onChange={(e) => setMaxApplications(e.target.value)}
          />
        </div>
        <button type="submit">Create Opportunity</button>
      </form>
    </div>
  );
};

export default CreateResearchOpportunity;
