import { useState } from "react";

import toast from "react-hot-toast";

import {
  loginUser
} from "../api/authApi";

function Login({
  onLoginSuccess,
  goToSignup
}) {

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const handleLogin = async () => {

    try {

      const response =
        await loginUser({

          email,
          password

        });

      localStorage.setItem(
        "token",
        response.data.token
      );

      toast.success(
        "Login Successful"
      );

      onLoginSuccess(
        response.data.token
      );

    } catch (error) {

      toast.error(

        error.response?.data?.detail ||

        "Login Failed"
      );
    }
  };

  return (

    <div className="auth-page">

      <div className="auth-card">

        <h1>
          Welcome Back
        </h1>

        <p>
          Login to continue using
          AI PDF Chatbot
        </p>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(
              e.target.value
            )
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
        />

        <button
          onClick={handleLogin}
        >
          Login
        </button>

        <span>

          Don't have an account?

          <strong
            onClick={goToSignup}
          >
            Sign Up
          </strong>

        </span>

      </div>

    </div>
  );
}

export default Login;