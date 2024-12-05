"use client";
import { useState } from "react";
import axios from "axios";
import logo from "@/assets/unt-logo.png";
import Image from "next/image";

const RegisterProfessor = () => {
  const [formData, setFormData] = useState({
    user: 1, // Assuming a default user ID for now
    first_name: "",
    last_name: "",
    password: "",
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

  // const handleFileChange = (e) => {
  //   setFormData({ ...formData, profile_picture: e.target.files[0] });
  // };

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
    <div className="container-fluid primary-background py-5">
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <div className="card p-5 shadow-sm">
              <div className="card-body">
                <h1 className="text-center text-success mb-4">
                  Register as Faculty Staff
                </h1>
                <form onSubmit={handleSubmit}>
                  <div className="mb-3">
                    <label htmlFor="first_name" className="form-label">
                      First Name:
                    </label>
                    <input
                      type="text"
                      id="first_name"
                      name="first_name"
                      value={formData.first_name}
                      onChange={handleChange}
                      required
                      className="form-control"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="last_name" className="form-label">
                      Last Name:
                    </label>
                    <input
                      type="text"
                      id="last_name"
                      name="last_name"
                      value={formData.last_name}
                      onChange={handleChange}
                      required
                      className="form-control"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="email" className="form-label">
                      Email:
                    </label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                      className="form-control"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="password" className="form-label">
                      Password:
                    </label>
                    <input
                      type="password"
                      id="password"
                      name="password"
                      value={formData.password}
                      onChange={handleChange}
                      required
                      className="form-control"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="department" className="form-label">
                      Department:
                    </label>
                    <input
                      type="text"
                      id="department"
                      name="department"
                      value={formData.department}
                      onChange={handleChange}
                      required
                      className="form-control"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="title" className="form-label">
                      Title:
                    </label>
                    <input
                      type="text"
                      id="title"
                      name="title"
                      value={formData.title}
                      onChange={handleChange}
                      required
                      className="form-control"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="office_location" className="form-label">
                      Office Location:
                    </label>
                    <input
                      type="text"
                      id="office_location"
                      name="office_location"
                      value={formData.office_location}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="phone_number" className="form-label">
                      Phone Number:
                    </label>
                    <input
                      type="text"
                      id="phone_number"
                      name="phone_number"
                      value={formData.phone_number}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="research_interests" className="form-label">
                      Research Interests:
                    </label>
                    <textarea
                      id="research_interests"
                      name="research_interests"
                      value={formData.research_interests}
                      onChange={handleChange}
                      className="form-control"
                      rows="4"
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="publications" className="form-label">
                      Publications:
                    </label>
                    <textarea
                      id="publications"
                      name="publications"
                      value={formData.publications}
                      onChange={handleChange}
                      className="form-control"
                      rows="4"
                    />
                  </div>

                  {/* <div className="mb-3">
              <label htmlFor="profile_picture" className="form-label">
                Profile Picture:
              </label>
              <input
                type="file"
                id="profile_picture"
                name="profile_picture"
                onChange={handleFileChange}
                className="form-control"
              />
            </div> */}

                  <div className="d-flex justify-content-center">
                    <button
                      type="submit"
                      disabled={uploading}
                      className="btn btn-success px-5"
                    >
                      {uploading ? "Submitting..." : "Submit"}
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <Image src={logo} alt="Landscape picture" className="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default RegisterProfessor;
