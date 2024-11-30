"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import axios from "axios";

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
    <div>
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <div>
          <label>Email:</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        {error && <p>{error}</p>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
