import { useState } from "react";

import toast from "react-hot-toast";

import {
  signupUser
} from "../api/authApi";

function Signup({
  goToLogin
}) {

  const [name, setName] =
    useState("");

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const handleSignup = async () => {

    try {

      await signupUser({

        name,
        email,
        password

      });

      toast.success(
        "Account Created Successfully"
      );

      goToLogin();

    } catch (error) {

      toast.error(

        error.response?.data?.detail ||

        "Signup Failed"
      );
    }
  };

  return (

    <div className="auth-page">

      <div className="auth-card">

        <h1>
          Create Account
        </h1>

        <p>
          Start chatting with your
          PDFs using AI
        </p>

        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) =>
            setName(
              e.target.value
            )
          }
        />

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
          onClick={handleSignup}
        >
          Sign Up
        </button>

        <span>

          Already have an account?

          <strong
            onClick={goToLogin}
          >
            Login
          </strong>

        </span>

      </div>

    </div>
  );
}

export default Signup;