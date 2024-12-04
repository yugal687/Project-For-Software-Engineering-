"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter, usePathname, useParams } from "next/navigation";
import axios from "axios";
import DashboardLayout from "@/components/facultyComponents/FacultyDashboardLayout";

const StudentsApplication = () => {
  const [data, setData] = useState("");
  const [error, setError] = useState(null);
  const router = useRouter();
  const params = useParams();
  const [opportunityID, setOpportunityID] = useState(null);
  const [selectedValue, setSelectedValue] = useState("");
  const [status, setStatus] = useState("");
  // const token = params.token;
  // const { id } = router.query.id;
  // const id = localStorage.getItem("user_id");

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem("access-token");
      const id = localStorage.getItem("user_id");

      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/professor/${id}/`,
          {
            headers: { Authorization: `Token ${token}` }, // Forward the authorization header
          }
        );
        const data = await response.json();
        console.log(data);
        setData(data);
      } catch (error) {
        setError(error);
      } finally {
        // setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleApplyClick = (opportunityId) => {
    setOpportunityID(opportunityId); // Set the research opportunity id when Apply button is clicked
  };

  const handleStatusChange = (e) => {
    setStatus(e.target.value); // Update status based on dropdown selection
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("status", selectedValue);
    console.log(selectedValue);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/professor/applications/${opportunityID}/update-status/`,
        {
          method: "PATCH", // Use PUT or PATCH depending on your API design
          headers: {
            "Content-Type": "application/json", // Sending JSON data
          },
          body: JSON.stringify({
            status: status, // Send the updated status
          }),
        }
      );

      if (response.ok) {
        alert("Form submitted successfully");
      } else {
        alert("Failed to submit form");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error submitting form");
    }
  };

  return (
    <div>
      <DashboardLayout>
        <div>
          {data &&
            data.research_posts.map((i) => {
              return (
                <div key={i.id}>
                  {i.students_applied.map((d) => {
                    return (
                      <div class="card my-3" key={d.id}>
                        <div class="card-body">
                          <h5 class="card-title"></h5>
                          <h6 class="card-subtitle mb-2 text-muted">
                            {d.student_name}
                          </h6>
                          <div>Applied for: {i.title}</div>
                          <p>applied on: {d.applied_at}</p>
                          <div>
                            Resume: <a href={d.resume}>Click here</a>
                          </div>
                          <div>
                            Status: <p>{d.status}</p>
                          </div>
                          <form onSubmit={handleSubmit}>
                            <select
                              class="form-select w-auto"
                              aria-label="Default select example"
                              value={status}
                              onChange={handleStatusChange}
                            >
                              <option defaultValue>
                                Open this select menu
                              </option>
                              <option value="pending">Pending</option>
                              <option value="accepted">Accepted</option>
                              <option value="rejected">Rejected</option>
                            </select>
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
                                    <h5
                                      class="modal-title"
                                      id="exampleModalLabel"
                                    >
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
                                        Confirm change Stasus
                                      </h2>

                                      <div className="text-center">
                                        <button
                                          type="submit"
                                          className="btn btn-primary w-50"
                                        >
                                          Submit
                                        </button>
                                      </div>
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

                            {/* <p class="card-text">{i.description}</p> */}
                          </form>
                          <button
                            type="submit"
                            data-bs-toggle="modal"
                            data-bs-target="#exampleModal"
                            onClick={() => handleApplyClick(d.id)}
                            class="btn btn-success mt-2 card-link"
                          >
                            Submit Status
                          </button>
                        </div>
                      </div>
                    );
                  })}
                </div>
              );
            })}
        </div>
      </DashboardLayout>
    </div>
  );
};

export default StudentsApplication;
