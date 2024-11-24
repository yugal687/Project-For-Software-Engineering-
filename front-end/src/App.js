
import React from 'react';
import './App.css';
// import ResearchOpportunityForm from './components/ResearchOpportunityForm';
import CreateResearchOpportunity from "./components/CreateResearchOpportunity";
import ListResearchOpportunities from './components/ListResearchOpportunities';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/LoginPage';


function App() {
  return (
    <div className="App">
    
      <Router>
        <Routes>
          <Route path="/" element={<CreateResearchOpportunity />} />
          <Route path="/list" element={<ListResearchOpportunities />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
