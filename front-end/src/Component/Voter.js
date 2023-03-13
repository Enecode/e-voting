import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import  getCookie  from 'django-react-csrftoken';
import DjangoCSRFToken from 'django-react-csrftoken';
import "./Voter.css";

function Voter() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    phoneNumber: "",
  });
  const [token, setToken] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(formData);
    const response = await fetch("/voter/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie('csrftoken'),
      },
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    console.log(data);
    const emailResponse = await fetch("/send-token-email/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: formData.email,
        token: data.token,
      }),
    });
    if (emailResponse.ok) {
      setShowModal(true);
    } else {
      setErrorMessage("Error sending token email");
    }
  };

  const handleTokenChange = (event) => {
    setToken(event.target.value);
  };

  const handleTokenValidation = async () => {
    const response = await fetch("/validate-token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
      }),
    });
    const data = await response.json();
    if (data.valid) {
      navigate("/party");
    } else {
      setErrorMessage("Invalid token");
    }
  };

  return (
    <div className="form-container">
      <p className="title">Welcome to Voter's Registration Portal </p>
      <p className="title-paragraph">Please fill in the form below to register as a voter</p>
      <form onSubmit={handleSubmit}>
        <DjangoCSRFToken />
          <label>
            First Name:
            <input
              required
              className="form-control"
              type="text"
              name="firstName"
              value={formData.firstName}
              onChange={handleInputChange}
            />
          </label>
          <label>
            Last Name:
            <input
              required
              className="form-control"
              type="text"
              name="lastName"
              value={formData.lastName}
              onChange={handleInputChange}
            />
          </label>
          <label>
            Email:
            <input
              required
              className="form-control"
              type="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
            />
          </label>
          <label>
            Phone Number:
            <input
              required
              type="tel"
              ClassName="form-control"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleInputChange}
            />
          </label>
          <button className="send-token-btn" type="submit">Send Token</button>
          {showModal && (
            <div>
              <label>
                Token:
                <input type="text" value={token} onChange={handleTokenChange} />
              </label>
              <button onClick={handleTokenValidation}>Validate Me</button>
            </div>
          )}
          {errorMessage && <p className="error">{ errorMessage}</p>}
      </form>
    </div>
  );
}

export default Voter;
