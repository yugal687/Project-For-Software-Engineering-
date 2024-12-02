"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import axios from "axios";
import { toast } from "react-hot-toast";

export async function loginStudent(email, password) {
  try {
    const response = await axios.post(
      "http://localhost:8000/api/student/login/",
      {
        email,
        password,
      },
      {
        withCredentials: true, // Include cookies in requests
      }
    );

    return response.data; // Handle the login response
  } catch (error) {
    console.error("Login failed:", error.response.data);
    throw error.response.data;
  }
}

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();
  const [data, setData] = useState([]);
  //   const [userID, setUserID]

  //   const handleLogin = async (e) => {
  //     e.preventDefault();
  //     try {
  //       await loginStudent(email, password);
  //       router.push('/student/dashboard'); // Redirect to the dashboard
  //     } catch (err) {
  //       setError(err.error || 'Login failed');
  //     }
  //   };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/student/login/",
        {
          email,
          password,
        },
        {
          withCredentials: true, // Include cookies in requests
        }
      );

      if (response.status == 200) {
        toast.success("You did it");

        router.push("/student/dashboard");
      }
      // Save the JWT token to local storage
      //   localStorage.setItem("access_token", response.data.access);
      //   localStorage.setItem("user_id", response.data.id);
      console.log(response.status);
      console.log(response.data);

      // setData(response.data);
      //   professor_id = response.data.professor_id;
      //   const path = "/student/dashboard";
      //   router.push(path);

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
