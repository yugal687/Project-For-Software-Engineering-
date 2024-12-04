"use client";
import DashboardLayout from "@/components/facultyComponents/FacultyDashboardLayout";
import { useParams } from "next/navigation";
import { useRouter } from "next/router";
import React, { useState, useEffect } from "react";

const page = () => {
  const [data, setData] = useState([]);
  const params = useParams();
  const id = params.id;

  useEffect(() => {
    const fetchData = async () => {
      // setIsLoading(true);
      //   const token = localStorage.getItem("access-token");
      //   const id = localStorage.getItem("user_id");

      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/professor/opportunity/${id}/`
          //   {
          //     headers: { Authorization: `Token ${token}` }, // Forward the authorization header
          //   }
        );
        const data = await response.json();
        // console.log(data.students_applied[0].student_name);
        setData(data);
      } catch (error) {
        // setError(error);
      } finally {
        // setIsLoading(false);
      }
    };

    fetchData();
  }, [id]);
  return (
    <>
      <DashboardLayout>
        <div>
          Students Applied:
          <div>
            {data.students_applied
              ? data.students_applied.map((v) => {
                  return (
                    <p key={v.id} className="text-dark">
                      {v.student_name}
                    </p>
                  );
                })
              : ""}
          </div>
        </div>
        <div class="card mt-3">
          <div class="card-body">
            <h5 class="card-title"></h5>
            <h6 class="card-subtitle mb-2 text-muted">{data.title}</h6>
            <p class="card-text">{data.description}</p>
            <p class="card-text">{data.deadline}</p>
            <p class="card-text">{data.posted_on}</p>
            <p class="card-text">{data.required_skills}</p>
            <p class="card-text">{data.research_tags}</p>
            <p class="card-text">{data.description}</p>
            <p class="card-text">{data.description}</p>
            <p class="card-text">{data.description}</p>
          </div>
        </div>
      </DashboardLayout>
    </>
  );
};

export default page;
