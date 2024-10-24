import DashboardLayout from "@/components/DashboardLayout";
import React from "react";

const page = () => {
  return (
    <DashboardLayout>
      <div>
        <section id="featured" className="bg-light py-5">
          <div className="container">
            <h3 className="text-center mb-4">Featured Research Projects</h3>
            <div className="row">
              <div className="col-md-4 mb-4">
                <div className="card h-100">
                  <div className="card-body">
                    <h5 className="card-title">AI in Healthcare</h5>
                    <p className="card-text">
                      Explore how artificial intelligence is revolutionizing the
                      healthcare industry.
                    </p>
                    <a href="#" className="btn btn-outline-primary">
                      Learn More
                    </a>
                  </div>
                </div>
              </div>
              <div className="col-md-4 mb-4">
                <div className="card h-100">
                  <div className="card-body">
                    <h5 className="card-title">Climate Change Research</h5>
                    <p className="card-text">
                      Join a team studying the effects of climate change on
                      biodiversity.
                    </p>
                    <a href="#" className="btn btn-outline-primary">
                      Learn More
                    </a>
                  </div>
                </div>
              </div>
              <div className="col-md-4 mb-4">
                <div className="card h-100">
                  <div className="card-body">
                    <h5 className="card-title">Quantum Computing</h5>
                    <p className="card-text">
                      Get involved in cutting-edge research on the future of
                      computing.
                    </p>
                    <a href="#" className="btn btn-outline-primary">
                      Learn More
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </DashboardLayout>
  );
};

export default page;
