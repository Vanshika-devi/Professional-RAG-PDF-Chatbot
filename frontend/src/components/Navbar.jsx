// frontend/src/components/Navbar.jsx

import { motion } from "framer-motion";

function Navbar() {

  return (
    <motion.div
      className="navbar"
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6 }}
    >

      <div className="logo-wrapper">

        <div className="logo-circle">
          AI
        </div>

        <div>
          <h1>RAG PDF Chatbot</h1>

          <p>
            AI Powered Document Intelligence Platform
          </p>
        </div>

      </div>

      <div className="nav-buttons">

        <button className="glass-btn">
          Dashboard
        </button>

        <button className="gradient-btn">
          Upgrade
        </button>

      </div>

    </motion.div>
  );
}

export default Navbar;