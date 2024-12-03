"use client";
import DashboardLayout from "@/components/studentComponents/DashboardLayout";
import React, { useEffect, useState } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";

const page = () => {
  const [formData, setFormData] = useState({
    student: "",
    research_opportunity: "",
    resume: null,
  });
  const [data, setData] = useState([]);
  const [StudentData, setStudentData] = useState([]);
  const [studentName, setStudentName] = useState(null);
  const [researchOpportunity, setResearchOpportunity] = useState(null);
  const [resume, setResume] = useState(null);
  const [rk, setRK] = useState("");
  const router = useRouter();

  const get_id = localStorage.getItem("user_id");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("student", studentName);
    formData.append("research_opportunity", researchOpportunity);
    formData.append("resume", resume);
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/student/opportunity/apply/",
        {
          method: "POST",
          //   headers: {
          //     "Content-Type": "multipart/form-data",
          //   },
          body: formData,
        }
      );

      if (response.ok) {
        alert("Form submitted successfully");
        router.push("/student/dashboard/opportunities/score");
        setFormData({
          student: "",
          research_opportunity: "",
          resume: null,
        });
      } else {
        alert("Failed to submit form");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error submitting form");
    }

    // Here you can handle form data or file upload logic, like sending it to an API
  };

  //   get score
  const get_score = async (e) => {
    e.preventDefault();
    const formData1 = new FormData();
    formData1.append("required_keywoards_front_end", rk);
    // formData1.append("research_opportunity", researchOpportunity);
    formData1.append("resume", resume);
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/student/my/getscore/",
        {
          method: "POST",
          //   headers: {
          //     "Content-Type": "multipart/form-data",
          //   },
          body: formData1,
        }
      );

      if (response.ok) {
        alert("Form submitted successfully");
        console.log(response);

        // setFormData({
        //   student: "",
        //   research_opportunity: "",
        //   resume: null,
        // });
      } else {
        alert("Failed to submit form");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error submitting form");
    }

    // Here you can handle form data or file upload logic, like sending it to an API
  };

  async function get_all_opportunities() {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/student/get-active-opportunities/`
    );

    setData(response.data);
    console.log(response.data);
  }
  async function get_student_detail() {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/student/${get_id}`
    );

    setStudentData(response.data);
    setStudentName(response.data.id);
    console.log(response.data);
  }
  const handleApplyClick = (opportunityId) => {
    setResearchOpportunity(opportunityId); // Set the research opportunity id when Apply button is clicked
  };
  useEffect(() => {
    get_all_opportunities();
    get_student_detail();
  }, []);
  return (
    <DashboardLayout>
      <div>
        <section id="featured" className="bg-light py-5">
          <div className="container">
            <h3 className="text-center mb-4">Featured Research Projects</h3>
            <div className="row">
              {data &&
                data.map((i) => {
                  return (
                    <div className="col-md-4 mb-4">
                      <div className="card h-100">
                        <div className="card-body">
                          <h5 className="card-title">Title: {i.title}</h5>
                          <p className="card-text">
                            Description:{i.description}
                          </p>
                          <p className="card-text">
                            Posted by: {i.professor_name}
                          </p>
                          <div className="d-flex">
                            <button
                              type="button"
                              class="btn btn-primary"
                              data-bs-toggle="modal"
                              data-bs-target="#exampleModal"
                              onClick={() => handleApplyClick(i.id)}
                            >
                              Apply
                            </button>
                            <button
                              type="button"
                              class="btn btn-primary"
                              data-bs-toggle="modal"
                              data-bs-target="#exampleModal2"
                            >
                              Get Score
                            </button>
                          </div>
                        </div>
                      </div>
                      {/* modal */}
                      <div
                        class="modal fade"
                        id="exampleModal"
                        tabindex="-1"
                        aria-labelledby="exampleModalLabel"
                        aria-hidden="true"
                      >
                        <div class="modal-dialog">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-title" id="exampleModalLabel">
                                Student Application
                              </h5>
                              <button
                                type="button"
                                class="btn-close"
                                data-bs-dismiss="modal"
                                aria-label="Close"
                              ></button>
                            </div>
                            <div class="modal-body">
                              <div className="container mt-5">
                                <h2 className="text-center mb-4">
                                  Student Application Form
                                </h2>
                                <form onSubmit={handleSubmit}>
                                  {/* Student Name Field */}
                                  <div className="mb-3">
                                    <label
                                      htmlFor="studentName"
                                      className="form-label"
                                    >
                                      Student Name
                                    </label>
                                    <input
                                      type="text"
                                      className="form-control"
                                      id="studentName"
                                      value={studentName}
                                      onChange={(e) =>
                                        setStudentName(e.target.value)
                                      }
                                    />
                                  </div>

                                  {/* Opportunity Name Field */}
                                  <div className="mb-3">
                                    <label
                                      htmlFor="opportunityName"
                                      className="form-label"
                                    >
                                      Opportunity Name
                                    </label>
                                    <input
                                      type="text"
                                      className="form-control"
                                      id="opportunityName"
                                      value={i.id}
                                      onChange={(e) =>
                                        setResearchOpportunity(e.target.value)
                                      }
                                    />
                                  </div>

                                  {/* Resume Upload Field */}
                                  <div className="mb-3">
                                    <label
                                      htmlFor="resume"
                                      className="form-label"
                                    >
                                      Upload Resume
                                    </label>
                                    <input
                                      type="file"
                                      className="form-control"
                                      id="resume"
                                      accept=".pdf,.docx"
                                      onChange={(e) =>
                                        setResume(e.target.files[0])
                                      }
                                      required
                                    />
                                  </div>

                                  {/* Submit Button */}
                                  <div className="text-center">
                                    <button
                                      type="submit"
                                      className="btn btn-primary w-50"
                                    >
                                      Submit
                                    </button>
                                  </div>
                                </form>
                              </div>
                            </div>
                            <div class="modal-footer">
                              <button
                                type="button"
                                class="btn btn-secondary"
                                data-bs-dismiss="modal"
                              >
                                Close
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                      {/* modal ends */}
                      <div
                        class="modal fade"
                        id="exampleModal2"
                        tabindex="-1"
                        aria-labelledby="exampleModalLabel"
                        aria-hidden="true"
                      >
                        <div class="modal-dialog">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-title" id="exampleModalLabel">
                                Student Application
                              </h5>
                              <button
                                type="button"
                                class="btn-close"
                                data-bs-dismiss="modal"
                                aria-label="Close"
                              ></button>
                            </div>
                            <div class="modal-body">
                              <div className="container mt-5">
                                <h2 className="text-center mb-4">
                                  Student Application Form
                                </h2>
                                <form onSubmit={get_score}>
                                  {/* Student Name Field */}

                                  {/* Opportunity Name Field */}
                                  <div className="mb-3">
                                    <label
                                      htmlFor="opportunityName"
                                      className="form-label"
                                    >
                                      Related Skills
                                    </label>
                                    <input
                                      type="text"
                                      className="form-control"
                                      id="keywords"
                                      value={data.required_skills}
                                      onChange={(e) => setRK(e.target.value)}
                                    />
                                  </div>

                                  {/* Resume Upload Field */}
                                  <div className="mb-3">
                                    <label
                                      htmlFor="resume"
                                      className="form-label"
                                    >
                                      Upload Resume
                                    </label>
                                    <input
                                      type="file"
                                      className="form-control"
                                      id="resume"
                                      accept=".pdf,.docx"
                                      onChange={(e) =>
                                        setResume(e.target.files[0])
                                      }
                                      required
                                    />
                                  </div>

                                  {/* Submit Button */}
                                  <div className="text-center">
                                    <button
                                      type="submit"
                                      className="btn btn-primary w-50"
                                    >
                                      Submit
                                    </button>
                                  </div>
                                </form>
                              </div>
                            </div>
                            <div class="modal-footer">
                              <button
                                type="button"
                                class="btn btn-secondary"
                                data-bs-dismiss="modal"
                              >
                                Close
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  );
                })}
            </div>
          </div>
        </section>
      </div>
    </DashboardLayout>
  );
};

export default page;
