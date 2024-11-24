import React, { useState } from 'react';
import axios from 'axios';

const ResearchOpportunityForm = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [deadline, setDeadline] = useState('');
    const [tags, setTags] = useState('');
    
    const handleSubmit = (e) => {
        e.preventDefault();

        // Prepare the data to send to the Django API
        const researchOpportunityData = {
            title: title,
            description: description,
            deadline: deadline,
            research_tags: tags,
            is_active: true
        };

        // Make the POST request to the Django API
        axios.post('http://127.0.0.1:8000/professor/api/researchopportunity/', researchOpportunityData)
            .then(response => {
                console.log('Research Opportunity Created:', response.data);
            })
            .catch(error => {
                console.error('There was an error creating the research opportunity!', error);
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="text" 
                placeholder="Title" 
                value={title}
                onChange={(e) => setTitle(e.target.value)} 
            />
            <textarea 
                placeholder="Description" 
                value={description}
                onChange={(e) => setDescription(e.target.value)} 
            />
            <input 
                type="date" 
                placeholder="Deadline" 
                value={deadline}
                onChange={(e) => setDeadline(e.target.value)} 
            />
            <input 
                type="text" 
                placeholder="Tags (comma separated)" 
                value={tags}
                onChange={(e) => setTags(e.target.value)} 
            />
            <button type="submit">Create Research Opportunity</button>
        </form>
    );
};

export default ResearchOpportunityForm;
