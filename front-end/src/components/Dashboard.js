import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ResearchOpportunitiesList = () => {
  const [opportunities, setOpportunities] = useState([]);

  useEffect(() => {
    axios
      .get('http://localhost:8000/professor/api/researchopportunities/')
      .then((response) => {
        setOpportunities(response.data);
      })
      .catch((error) => {
        console.error('There was an error fetching the opportunities!', error);
      });
  }, []);

  return (
    <div>
      <h2>Research Opportunities</h2>
      <ul>
        {opportunities.map((opportunity) => (
          <li key={opportunity.id}>
            <h3>{opportunity.title}</h3>
            <p>{opportunity.description}</p>
            <p>Deadline: {new Date(opportunity.deadline).toLocaleString()}</p>
            <p>Status: {opportunity.is_active ? 'Active' : 'Closed'}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ResearchOpportunitiesList;
