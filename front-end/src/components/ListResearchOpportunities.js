import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ListResearchOpportunities() {
  const [opportunities, setOpportunities] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/professor/api/researchopportunities/')
      .then(response => {
        setOpportunities(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the opportunities!', error);
      });
  }, []);

  return (
    <div>
      <h1>Research Opportunities</h1>
      <ul>
        {opportunities.map(opportunity => (
          <li key={opportunity.id}>{opportunity.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default ListResearchOpportunities;
