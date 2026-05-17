import {
  useEffect,
  useState
} from "react";

import Login from "./pages/Login";

import Signup from "./pages/Signup";

import Home from "./pages/Home";

import "./styles/global.css";

function App() {

  const [currentPage,
    setCurrentPage] =
    useState("login");

  const [isAuthenticated,
    setIsAuthenticated] =
    useState(false);

  useEffect(() => {

    const token =
      localStorage.getItem(
        "token"
      );

    if (token) {

      setIsAuthenticated(true);
    }

  }, []);

  const handleLoginSuccess =
    (token) => {

      localStorage.setItem(
        "token",
        token
      );

      setIsAuthenticated(true);
    };

  if (!isAuthenticated) {

    return (

      currentPage === "login"

        ? (

          <Login
            onLoginSuccess={
              handleLoginSuccess
            }

            goToSignup={() =>
              setCurrentPage(
                "signup"
              )
            }
          />

        ) : (

          <Signup
            goToLogin={() =>
              setCurrentPage(
                "login"
              )
            }
          />

        )
    );
  }

  return (

    <div className="app">

      <Home />

    </div>
  );
}

export default App;