import React, { useState } from "react";
import axios from "axios";

const VoterVerification = ({ history }) => {
  const [vin, setVin] = useState("");
  const [error, setError] = useState(null);

  const handleVinChange = (e) => {
    setVin(e.target.value);
  };

  const handleVerification = async () => {
    try {
      const response = await axios.get("/v2/api/identity/ng/pvc", {
        params: { vin },
      });
      if (response.data.isVerified) {
        history.push("/party");
      } else {
        setError("Incorrect VIN");
      }
    } catch (error) {
      console.error(error);
      setError("An error occurred while verifying your VIN");
    }
  };

  return (
    <div>
      <h2>Verify your Voter Identification Number</h2>
      <input type="text" placeholder="Enter your VIN" onChange={handleVinChange} />
      <button onClick={handleVerification}>Verify</button>
      {error && <p>{error}</p>}
    </div>
  );
};

export default VoterVerification;
