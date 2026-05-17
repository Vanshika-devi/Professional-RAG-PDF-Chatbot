import {
  useState,
  useEffect
} from "react";

import { motion } from "framer-motion";

import toast from "react-hot-toast";

import {
  uploadPDF
} from "../api/authApi";

function UploadBox() {

  const [file, setFile] =
    useState(null);

  const [uploadedFile,
    setUploadedFile] =
    useState("");

  const [uploading,
    setUploading] =
    useState(false);

  useEffect(() => {

    const savedFile =
      localStorage.getItem(
        "activePDF"
      );

    if (savedFile) {

      setUploadedFile(
        savedFile
      );
    }

  }, []);

  const handleUpload =
    async () => {

      if (!file) {

        toast.error(
          "Please Select a PDF"
        );

        return;
      }

      try {

        setUploading(true);

        toast.loading(
          "Processing PDF...",
          {
            id: "upload"
          }
        );

        const formData =
          new FormData();

        formData.append(
          "file",
          file
        );

        await uploadPDF(
          formData
        );

        setUploadedFile(
          file.name
        );

        localStorage.setItem(
          "activePDF",
          file.name
        );

        toast.success(
          "PDF Uploaded Successfully",
          {
            id: "upload"
          }
        );

      } catch (error) {

        toast.error(
          "Upload Failed",
          {
            id: "upload"
          }
        );

      } finally {

        setUploading(false);
      }
    };

  return (

    <motion.div
      className="upload-box"
      initial={{
        opacity: 0,
        y: 40
      }}
      animate={{
        opacity: 1,
        y: 0
      }}
    >

      <div className="upload-left">

        <div className="upload-badge">
          AI PDF ANALYZER
        </div>

        <h2>
          Upload PDF & Chat
          With AI
        </h2>

        <p>
          Upload documents and
          ask intelligent
          contextual questions.
        </p>

      </div>

      <div className="upload-right">

        <div className="upload-card">

          <div className="upload-icon">
            📄
          </div>

          <h3>
            Upload PDF
          </h3>

          <label className="custom-file-upload">

            <input
              type="file"
              accept="application/pdf"
              onChange={(e) =>
                setFile(
                  e.target.files[0]
                )
              }
            />

            Choose PDF

          </label>

          {
            file && (

              <div className="file-preview">

                <div className="file-label">
                  Selected File
                </div>

                <div className="file-name">
                  {file.name}
                </div>

              </div>
            )
          }

          {
            uploadedFile && (

              <div className="uploaded-file-box">

                <div className="uploaded-label">
                  Active PDF
                </div>

                <div className="uploaded-name">
                  {uploadedFile}
                </div>

              </div>
            )
          }

          <button
            className="upload-btn"
            onClick={handleUpload}
            disabled={uploading}
          >

            {
              uploading
                ? "Processing..."
                : "Upload PDF"
            }

          </button>

        </div>

      </div>

    </motion.div>
  );
}

export default UploadBox;