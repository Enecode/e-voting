import './App.css';
import Verification from './Component/Verification';
import Voter from "./Component/Voter";
import PartyPage from './Component/PartyPage';
import VotinPage from "./Component/VotinPage";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import Result from "./Component/Result";


function App() {

  return (
        <Router>
          <Routes>
            <Route path="/" element={<Voter />} />
            <Route path="/VotinPage" element={<PartyPage />} />
            <Route path="/Result" element={<VotinPage />} />
            <Route path="/PartyPage" element={<PartyPage />} />
            <Route path="/Verification" element={<Verification />} />
            <Route path="/VotinPage" element={<Result />} />
          </Routes>
        </Router>
  );
}

export default App;