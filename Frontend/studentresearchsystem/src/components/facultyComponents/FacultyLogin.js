// "use client";
// import { useState } from "react";
// import { useRouter } from "next/navigation";
// import axios from "axios";

// export default function Login() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [error, setError] = useState("");
//   const router = useRouter();
//   const [data, setData] = useState([]);
//   //   const [userID, setUserID]

//   const handleLogin = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post(
//         "http://localhost:8000/api/professor/login/",
//         {
//           email,
//           password,
//         }
//       );
//       // Save the JWT token to local storage
//     //   localStorage.setItem("access_token", response.data.access);
//     //   localStorage.setItem("user_id", response.data.professor_id);

//       //   setData(response.data);
//       //   professor_id = response.data.professor_id;
//       router.push("/faculty/dashboard");

//       //   router.push(`/faculty/dashboard/${response.data && professor_id}`);
//     } catch (error) {
//       setError("Invalid credentials");
//     }
//   };

//   return (
//     <div>
//       <h1>Login</h1>
//       <form onSubmit={handleLogin}>
//         <div>
//           <label>Email:</label>
//           <input
//             type="text"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//           />
//         </div>
//         <div>
//           <label>Password</label>
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//           />
//         </div>
//         {error && <p>{error}</p>}
//         <button type="submit">Login</button>
//       </form>
//     </div>
//   );
// }

"use client";
import { useState } from "react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      // Step 1: Fetch CSRF token
      const csrfResponse = await fetch(
        "http://127.0.0.1:8000/api/professor/csrf/"
      );
      const csrfData = await csrfResponse.json();
      const csrfToken = csrfData.csrfToken;

      // Step 2: Send login request with credentials and CSRF token
      const response = await fetch(
        "http://127.0.0.1:8000/api/professor/login/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
          credentials: "include", // Include cookies in the request
          body: JSON.stringify({ email, password }),
        }
      );

      if (response.ok) {
        const data = await response.json();
        alert(`Welcome, ${data.professor_email}`);
        // Optionally, redirect to the dashboard
        window.location.href = "/faculty/dashboard";
      } else {
        const errorData = await response.json();
        setError(errorData.error || "Invalid credentials");
      }
    } catch (err) {
      setError("Something went wrong");
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <div>
        <label>Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>
      <button type="submit">Login</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );
}
