"use client";
import { useState } from "react";
import axios from "axios";

const RegisterProfessor = () => {
  const [formData, setFormData] = useState({
    user: 1, // Assuming a default user ID for now
    first_name: "",
    last_name: "",
    department: "",
    title: "",
    office_location: "",
    phone_number: "",
    research_interests: "",
    publications: "",
    // profile_picture: null, // For file upload
    posted_opportunities_count: 0,
  });

  const [uploading, setUploading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  //   const handleFileChange = (e) => {
  //     setFormData({ ...formData, profile_picture: e.target.files[0] });
  //   };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // setUploading(true);

    // Prepare form data for API submission
    const data = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      data.append(key, value);
    });

    try {
      // Replace '/api/professors/' with your actual API endpoint
      const response = await axios.post(
        "http://127.0.0.1:8000/api/professor/",
        data,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );
      alert("Professor registered successfully!");
      console.log(response.data);
    } catch (error) {
      console.error("Error registering professor:", error);
      alert("Failed to register professor. Please try again.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "20px" }}>
      <h1>Register Professor</h1>
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input
            type="text"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <label>
          Last Name:
          <input
            type="text"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <label>
          Department:
          <input
            type="text"
            name="department"
            value={formData.department}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <label>
          Title:
          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <label>
          Office Location:
          <input
            type="text"
            name="office_location"
            value={formData.office_location}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Phone Number:
          <input
            type="text"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Research Interests:
          <textarea
            name="research_interests"
            value={formData.research_interests}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Publications:
          <textarea
            name="publications"
            value={formData.publications}
            onChange={handleChange}
          />
        </label>
        <br />
        {/* <label>
          Profile Picture:
          <input
            type="file"
            name="profile_picture"
            onChange={handleFileChange}
          />
        </label> */}
        <br />
        <button type="submit" disabled={uploading}>
          {uploading ? "Submitting..." : "Submit"}
        </button>
      </form>
    </div>
  );
};

export default RegisterProfessor;
