"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import axios from "axios";
import Navbar from "../Navbar";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();
  const [data, setData] = useState([]);
  //   const [userID, setUserID]

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/professor/login/",
        {
          email,
          password,
        }
      );
      // Save the JWT token to local storage
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("user_id", response.data.id);

      //   setData(response.data);
      //   professor_id = response.data.professor_id;
      const path = "/faculty/dashboard";
      router.push(path);

      //   router.push(`/faculty/dashboard/${response.data && professor_id}`);
    } catch (error) {
      setError("Invalid credentials");
    }
  };

  return (
    //   <div>
    //     <h1>Login</h1>
    //     <form onSubmit={handleLogin}>
    //       <div>
    //         <label>Email:</label>
    //         <input
    //           type="text"
    //           value={email}
    //           onChange={(e) => setEmail(e.target.value)}
    //         />
    //       </div>
    //       <div>
    //         <label>Password</label>
    //         <input
    //           type="password"
    //           value={password}
    //           onChange={(e) => setPassword(e.target.value)}
    //         />
    //       </div>
    //       {error && <p>{error}</p>}
    //       <button type="submit">Login</button>
    //     </form>
    //   </div>
    // );
    <>
      <Navbar />
      <div
        className="d-flex justify-content-center align-items-center min-vh-100"
        style={{ backgroundColor: "#006a00" }}
      >
        <div className="card p-4" style={{ width: "100%", maxWidth: "400px" }}>
          <h3 className="text-center mb-4" style={{ color: "#006a00" }}>
            Faculty Login
          </h3>
          <form onSubmit={handleLogin}>
            {/* Email Field */}
            <div className="mb-3">
              <label htmlFor="email" className="form-label">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
                required
              />
            </div>

            {/* Password Field */}
            <div className="mb-3">
              <label htmlFor="password" className="form-label">
                Password
              </label>
              <input
                type="password"
                className="form-control"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter your password"
                required
              />
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              className="btn primary-background primary-color w-100"
              style={{ backgroundColor: "#006a00", color: "#ffffff" }}
            >
              Login
            </button>
          </form>

          <div className="text-center mt-3">
            <p className="primary-color">Don't have an account? </p>
            <div>
              <a className="primary-color" href="/faculty/register">
                Register here
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
