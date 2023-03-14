import React, { useState } from 'react';
import axios from 'axios';

const Verification = () => {
  const [email, setEmail] = useState('');
  const [token, setToken] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get('/api/verifications/', { email });
      setToken(response.data.token);
    } catch (error) {
      setError(error.response.data.detail);
    }
  };

  const handleVerification = async (event) => {
    event.preventDefault();
    try {
      await axios.put('/api/verifications/', { token });
      window.location.href = '/party-page'; // Redirect to party page on successful verification
    } catch (error) {
      setError(error.response.data.detail);
    }
  };

  return (
    <div className='verification-container'>
      {!token && (
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Enter your email address:</label>
          <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <button type="submit">Send Token</button>
        </form>
      )}
      {token && (
        <form onSubmit={handleVerification}>
          <label htmlFor="token">Enter your token:</label>
          <input type="text" id="token" value={token} onChange={(e) => setToken(e.target.value)} />
          <button type="submit">Verify Token</button>
        </form>
      )}
      {error && <p>{error}</p>}
    </div>
  );
};

export default Verification;
