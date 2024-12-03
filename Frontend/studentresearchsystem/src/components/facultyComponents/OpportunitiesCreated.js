"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter, usePathname, useParams } from "next/navigation";
import axios from "axios";
import DashboardLayout from "@/components/facultyComponents/FacultyDashboardLayout";

const OpportunitiesCreated = () => {
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
    <DashboardLayout>
      <div>
        <div className="pt-3 pb-2 mb-3 border-bottom px-2">
          Faculty's Created Opportunities List
        </div>
        <Link href="/faculty/dashboard/opportunities/create">
          <button className="btn btn-success">Create Opportunity</button>
        </Link>

        {data &&
          data.research_posts.map((i) => {
            return (
              <div class="card mt-3">
                <div class="card-body">
                  <h5 class="card-title"></h5>
                  <h6 class="card-subtitle mb-2 text-muted">{i.title}</h6>
                  <p class="card-text">{i.description}</p>
                  <Link
                    href={`/faculty/dashboard/opportunities/${i.id}`}
                    class="btn primary-background text-white"
                  >
                    View Detail
                  </Link>
                </div>
              </div>
            );
          })}
      </div>
    </DashboardLayout>
  );
};

export default OpportunitiesCreated;
