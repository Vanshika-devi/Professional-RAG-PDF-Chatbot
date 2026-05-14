// frontend/src/components/UploadBox.jsx

import { motion } from "framer-motion";
import { uploadPDF } from "../api/ragApi";

function UploadBox() {

  const handleUpload = async (e) => {

    const file = e.target.files[0];

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {

      await uploadPDF(formData);

      alert("PDF Uploaded Successfully");

    } catch (error) {

      alert("Upload Failed");
    }
  };

  return (
    <motion.div
      className="upload-box"
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.7 }}
    >

      <div className="upload-left">

        <div className="upload-badge">
          AI PDF ANALYZER
        </div>

        <h2>
          Upload PDF & Chat With AI
        </h2>

        <p>
          Upload documents and get intelligent contextual answers instantly using RAG pipelines and semantic search.
        </p>

        <div className="feature-tags">

          <span>FastAPI</span>
          <span>LangChain</span>
          <span>ChromaDB</span>
          <span>Ollama</span>

        </div>

      </div>

      <div className="upload-right">

        <div className="upload-card">

          <div className="upload-icon">
            📄
          </div>

          <h3>Choose PDF File</h3>

          <input
            type="file"
            accept="application/pdf"
            onChange={handleUpload}
          />

        </div>

      </div>

    </motion.div>
  );
}

export default UploadBox;