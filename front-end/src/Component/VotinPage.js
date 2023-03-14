import React, { useState, useEffect } from 'react';
import Modal from 'react-modal';
import {useNavigate} from "react-router-dom";

function VotingPage() {
  const [parties, setParties] = useState([]);
  const [selectedParty, setSelectedParty] = useState(null);
  const [voterDetails, setVoterDetails] = useState(null);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const navigate = useNavigate();


  useEffect(() => {
    fetch('vote/')
      .then(response => response.json())
      .then(data => setParties(data));
  }, []);

  const fetchParties = () => {
    fetch('vote/')
      .then(response => response.json())
      .then(data => setParties(data));
  };

  const openModal = (party) => {
    setSelectedParty(party);
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
    setVoterDetails(null);
  };

  const handleVoterDetailsSubmit = (event) => {
    event.preventDefault();
    fetch('voter/')
      .then(response => response.json())
      .then(data => setVoterDetails(data));
  };

  const handleValidationSubmit = (event) => {
    event.preventDefault();
    fetch('verification/')
      .then(response => response.json())
      .then(data => {
        if (data.isValid) {

          navigate('/result');
        } else {
          alert('Invalid voter details!');
        }
      });
  };

  return (
    <div>
      <h1>Voting Page</h1>
      {parties.map(party => (
        <div key={party.id}>
          <h2>{party.name}</h2>
          <button onClick={() => openModal(party)}>Vote</button>
        </div>
      ))}
      <Modal isOpen={modalIsOpen} onRequestClose={closeModal}>
        {voterDetails ? (
          <div>
            <h2>Confirm voter details:</h2>
            <p>Name: {voterDetails.name}</p>
            <p>ID: {voterDetails.id}</p>
            <button onClick={handleValidationSubmit}>Confirm</button>
          </div>
        ) : (
          <div>
            <h2>Enter your voter details:</h2>
            <form onSubmit={handleVoterDetailsSubmit}>
              <label>
                Name:
                <input type="text" />
              </label>
              <br />
              <label>
                ID:
                <input type="text" />
              </label>
              <br />
              <button type="submit">Submit</button>
            </form>
          </div>
        )}
      </Modal>
    </div>
  );
}

export default VotingPage;