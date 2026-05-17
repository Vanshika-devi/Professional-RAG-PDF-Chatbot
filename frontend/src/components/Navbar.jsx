import { motion } from "framer-motion";

import toast from "react-hot-toast";

function Navbar() {

  const token =
    localStorage.getItem(
      "token"
    );

  const handleLogout = () => {

    localStorage.removeItem(
      "token"
    );

    toast.success(
      "Logged Out Successfully"
    );

    window.location.reload();
  };

  return (

    <motion.div
      className="navbar"
      initial={{
        y: -50,
        opacity: 0
      }}
      animate={{
        y: 0,
        opacity: 1
      }}
      transition={{
        duration: 0.5
      }}
    >

      <div className="logo-section">

        <div className="logo-circle">
          AI
        </div>

        <div>

          <h1>
            RAG PDF Chatbot
          </h1>

          <p>
            AI Powered Document
            Intelligence Platform
          </p>

        </div>

      </div>

      <div className="nav-buttons">

        {
          token ? (

            <button
              className="signup-btn"
              onClick={handleLogout}
            >
              Logout
            </button>

          ) : null
        }

      </div>

    </motion.div>
  );
}

export default Navbar;