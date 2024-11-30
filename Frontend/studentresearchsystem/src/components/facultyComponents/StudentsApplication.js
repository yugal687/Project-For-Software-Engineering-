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
  // const token = params.token;
  // const { id } = router.query.id;
  // const id = localStorage.getItem("user_id");

  useEffect(() => {
    const fetchData = async () => {
      // setIsLoading(true);
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
  return (
    <div>
      <DashboardLayout>
        <div>
          {data &&
            data.research_posts.map((i) => {
              return (
                <>
                  {i.students_applied.map((d) => {
                    return (
                      <div class="card">
                        <div class="card-body">
                          <h5 class="card-title"></h5>
                          <h6 class="card-subtitle mb-2 text-muted">
                            {d.student_name}
                          </h6>
                          {/* <p class="card-text">{i.description}</p> */}
                          <a href="#" class="card-link">
                            Card link
                          </a>
                          <a href="#" class="card-link">
                            Another link
                          </a>
                        </div>
                      </div>
                    );
                  })}
                </>
              );
            })}
        </div>
      </DashboardLayout>
    </div>
  );
};

export default StudentsApplication;
