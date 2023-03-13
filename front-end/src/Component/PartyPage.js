import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import './Partypage.css';
// import apcimage from '../../../party_symbols/APC.png';
// import pdpimage from '../../../party_symbols/APC.png';
// import image from '../../../party_symbols/APC.png';

function PartyPage() {
  const [parties, setParties] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('/party/')
      .then(response => response.json())
      .then(data => setParties(data));
  }, []);

  return (
    <div className='party-container'> 
      <h1 className='party-title'>Political Parties</h1>
      {parties.map(party => (
        <div key={party.id}>
          <h2 className='party-name'>{party.name}</h2>
          <img className='party-image' src={party.logo} alt={party.name} />
          <p className='party-description'>{party.description}</p>
          <Link to={`/Result/${party.id}`}>
            <button className='select-party-page' onClick={()=> navigate("/Result")}>Select</button>
          </Link>
        </div>
      ))}
    </div>
  );
}

export default PartyPage;