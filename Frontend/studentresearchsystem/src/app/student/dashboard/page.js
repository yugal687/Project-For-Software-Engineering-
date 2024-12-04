"use client";

import React, { useState, useEffect } from "react";
import Dashboard from "@/components/DashboardLayout";

const Page = () => {
  const [analysisResults, setAnalysisResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');

  // Function to fetch analysis results
  const fetchAnalysisResults = async () => {
    console.log('Fetching analysis results...');
    setLoading(true);
    try {
      console.log('Making API request...');
      const response = await fetch('http://localhost:8000/api/student/1/analyze-resume/', {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
        },
      });
      console.log('Response received:', response.status);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log('Data received:', data);
      setAnalysisResults(data.results);
      setError(null);
    } catch (err) {
      console.error('Error fetching results:', err);
      setError(`Failed to fetch analysis results: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Handle resume upload
  const handleResumeUpload = async (event) => {
    event.preventDefault();
    const file = event.target.resumeUpload.files[0];
    if (!file) {
      setUploadStatus('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('resume', file);

    try {
      setUploadStatus('Uploading...');
      console.log('Uploading resume...');
      const response = await fetch('http://localhost:8000/api/student/1/upload-resume/', {
        method: 'POST',
        body: formData,
      });

      console.log('Upload response:', response.status);
      if (response.ok) {
        setUploadStatus('Resume uploaded successfully!');
        // Fetch new analysis after upload
        fetchAnalysisResults();
      } else {
        const errorText = await response.text();
        console.error('Upload error:', errorText);
        setUploadStatus('Failed to upload resume: ' + errorText);
      }
    } catch (err) {
      console.error('Upload error:', err);
      setUploadStatus('Error uploading resume: ' + err.message);
    }
  };

  useEffect(() => {
    console.log('Component mounted, fetching initial results...');
    fetchAnalysisResults();
  }, []);

  return (
    <div>
      <Dashboard>
        <div className="pt-3 pb-2 mb-3 border-bottom">
          <h2>Student Dashboard</h2>
        </div>

        {/* Profile Information */}
        <section className="mb-4">
          <h4>Profile Information</h4>
          <div className="card p-3 mb-4">
            <div className="row">
              <div className="col-md-6">
                <p>
                  <strong>Name:</strong> James Bond
                </p>
                <p>
                  <strong>Email:</strong> johndoe@example.com
                </p>
                <p>
                  <strong>Major:</strong> Computer Science
                </p>
              </div>
              <div className="col-md-6">
                <p>
                  <strong>Year:</strong> Senior
                </p>
                <p>
                  <strong>University:</strong> University of North Texas
                </p>
                <p>
                  <strong>GPA:</strong> 3.8
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Resume Upload */}
        <section className="mb-4">
          <h4>Upload Your Resume</h4>
          <div className="card p-3">
            <form onSubmit={handleResumeUpload}>
              <div className="mb-3">
                <label htmlFor="resumeUpload" className="form-label">
                  Select resume file (PDF or DOCX):
                </label>
                <input
                  className="form-control"
                  type="file"
                  id="resumeUpload"
                  name="resumeUpload"
                  accept=".pdf,.doc,.docx"
                />
              </div>
              <button type="submit" className="btn btn-primary">
                Upload Resume
              </button>
              {uploadStatus && (
                <div className={`alert mt-3 ${uploadStatus.includes('success') ? 'alert-success' : 'alert-info'}`}>
                  {uploadStatus}
                </div>
              )}
            </form>
          </div>
        </section>

        {/* Resume Analysis Section */}
        <section className="mb-4">
          <h4>Resume Analysis</h4>
          <div className="card p-3">
            {loading ? (
              <div className="text-center">
                <div className="spinner-border text-primary" role="status">
                  <span className="visually-hidden">Loading...</span>
                </div>
              </div>
            ) : error ? (
              <div className="alert alert-danger" role="alert">
                {error}
              </div>
            ) : analysisResults ? (
              <div>
                {analysisResults.map((result) => (
                  <div key={result.opportunity_id} className="mb-4 border-bottom pb-3">
                    <h5>{result.opportunity_title}</h5>
                    <div className="mb-3">
                      <div className="d-flex justify-content-between align-items-center mb-1">
                        <strong>Overall Match:</strong>
                        <span className={`badge ${result.overall_score >= 70 ? 'bg-success' : 'bg-warning'}`}>
                          {result.overall_score}%
                        </span>
                      </div>
                      <div className="progress" style={{ height: "20px" }}>
                        <div
                          className="progress-bar"
                          role="progressbar"
                          style={{ width: `${result.overall_score}%` }}
                          aria-valuenow={result.overall_score}
                          aria-valuemin="0"
                          aria-valuemax="100"
                        />
                      </div>
                    </div>
                    
                    <div className="row">
                      <div className="col-md-6">
                        <h6>Detailed Scores:</h6>
                        <ul className="list-unstyled">
                          {Object.entries(result.detailed_scores).map(([category, score]) => (
                            <li key={category}>
                              {category.replace('_', ' ').charAt(0).toUpperCase() + category.slice(1)}: {score}%
                            </li>
                          ))}
                        </ul>
                      </div>
                      <div className="col-md-6">
                        <h6>Recommendations:</h6>
                        {result.recommendations.length > 0 ? (
                          <ul className="text-muted">
                            {result.recommendations.map((rec, i) => (
                              <li key={i}>{rec}</li>
                            ))}
                          </ul>
                        ) : (
                          <p className="text-success">Great match! No improvements needed.</p>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p>No analysis results available. Please upload your resume.</p>
            )}
          </div>
        </section>
      </Dashboard>
    </div>
  );
};

export default Page;
