import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const uploadPDF = async (formData) => {
  return API.post("/upload", formData);
};

export const askQuestion = async (question) => {
  return API.post("/ask", {
    question
  });
};