import axios from "axios";

const API = axios.create({

  baseURL:
    import.meta.env.VITE_API_URL ||
    "http://127.0.0.1:8000"

});

API.interceptors.request.use(

  (config) => {

    const token =
      localStorage.getItem(
        "token"
      );

    if (token) {

      config.headers.Authorization =
        `Bearer ${token}`;
    }

    return config;
  }

);

export const signupUser =
  async (userData) => {

    return API.post(
      "/signup",
      userData
    );
  };

export const loginUser =
  async (userData) => {

    return API.post(
      "/login",
      userData
    );
  };

export const uploadPDF =
  async (formData) => {

    return API.post(
      "/upload",
      formData
    );
  };

export const askQuestion =
  async (question) => {

    return API.post(
      "/ask",
      {
        question
      }
    );
  };

export default API;