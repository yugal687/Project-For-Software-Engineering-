"use client";
import React, { useEffect, useState } from "react";
import Dashboard from "@/components/facultyComponents/FacultyDashboardLayout";
import Link from "next/link";
import { useRouter, usePathname, useParams } from "next/navigation";
import axios from "axios";

const page = ({ data }) => {
  return (
    <div>
      <Dashboard data={data}>
        {/* Profile Information */}
        <section className="mb-4">
          <h4>Profile Information</h4>
          <div className="card p-3 mb-4">
            <div className="row">
              <div className="col-md-6">
                <p>
                  <strong>Name:</strong> {data.first_name} {data.last_name}
                </p>
                <p>
                  <strong>Email:</strong> {data.email}
                </p>
                <p>
                  <strong>Major:</strong> {data.department}
                </p>
              </div>
              <div className="col-md-6">
                <p>
                  <strong>Year:</strong> Senior
                </p>
                <p>
                  <strong>University:</strong> University of North Texas
                </p>
                <p>
                  <strong>GPA:</strong> 3.8
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Resume Upload */}
        <section className="mb-4">
          <h4>Posted Research</h4>
        </section>
      </Dashboard>
    </div>
  );
};

export default page;
