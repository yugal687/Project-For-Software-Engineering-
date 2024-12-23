"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
// import { useRouter } from "next/compat/router";

import axios from "axios";

const FacultyLogin = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();
  //   const pathname = usePathname();

  // useEffect(() => {
  //   // Prefetch the dashboard page
  //   router.prefetch("/dashboard");
  // }, [router]);

  const handleLogin = async (e) => {
    e.preventDefault();

    const response = await axios.post(
      "http://127.0.0.1:8000/api/student/login/",
      {
        email,
        password,
      }
    );

    if (response.status === 200) {
      // Store user data in state or localStorage if needed
      console.log(response);
      router.push("/student/dashboard");
    } else {
      setError("Invalid credentials. Please try again.");
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
      }}
    >
      <form onSubmit={handleLogin} style={{ maxWidth: "400px", width: "100%" }}>
        <h2>Student Login</h2>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
          />
        </div>
        <button type="submit" style={{ width: "100%", padding: "10px" }}>
          Login
        </button>
      </form>
    </div>
  );
};

export default FacultyLogin;
