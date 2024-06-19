Introduction

The Weather Data Ingestion and API Project aims to streamline the process of ingesting, processing, and accessing weather data. This project involves transferring raw weather data from text files into a SQLite database, performing data analysis to generate yearly statistics, and providing an API for accessing the processed data. The project is designed to be user-friendly, with automatic Swagger/OpenAPI documentation to facilitate API usage.

Steps of Execution

1. Clone the Repository:
  Download the project files from the GitHub repository.

    git clone https://github.com/your-username/your-repository.git
    cd your-repository

2. Set Up a Virtual Environment:
  Create and activate a virtual environment to manage project dependencies.

    python -m venv myenv
    source myenv/bin/activate

3. Install Required Packages:
  Install all necessary Python packages specified in the requirements.txt file.

    pip install -r requirements.txt

4. Data Ingestion:
  Ensure the raw weather data text files are located in the wx_data folder.
  Run the data ingestion script to load data into the SQLite database and log the process.

    python data_ingestion.py

5. Data Analysis:
  Run the data analysis script to calculate yearly weather statistics and store them in the database.

    python data_analysis.py

6. Start the API:
  Launch the Flask application to serve the API.

    python app.py

  Access the API documentation by navigating to http://127.0.0.1:5000/ in your browser.

7. Run Unit Tests:
  Execute the unit tests to ensure the API endpoints function correctly.

    python test_app.py






