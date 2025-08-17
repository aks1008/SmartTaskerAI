# SmartTaskerAI

## Overview
SmartTaskerAI is an intelligent task management system designed to streamline workflows and enhance productivity using AI-driven insights.

## Features
1. **Dashboard for Pending Task List**: View and manage all your pending tasks in one place.
2. **Smart Chat Bot to Assist Tasks**: Get real-time assistance and task suggestions from an AI-powered chatbot.
3. **Insightful Dashboard**: Gain actionable insights into your tasks and productivity through a comprehensive analytics dashboard.

## Technology Stack
- **Frontend**: Angular 15+
- **Backend**: Flask (Python)
- **Database**: SQLite
- **AI Integration**: Google Gemini AI
- **API Documentation**: Swagger/OpenAPI

## System Design
1. Web APP developed using Angular for the frontend and Flask for the backend.
2. Utilizes a SQLite database for data storage and management.
3. Integrates with Google Gemini AI for intelligent task management.
4. Implements a RESTful API for seamless communication.
5. Model Context Protocol (MCP) for efficient data handling.

<img width="1878" height="1016" alt="image" src="https://github.com/user-attachments/assets/7d5ec88a-bf23-4385-9ac3-de99067c02f4" />

## Front End UI code GitHub Repo
   ```bash
   git clone https://github.com/aks1008/smart-student-management.git
   ```

## API Documentation
The API documentation is available via Swagger UI at:
http://127.0.0.1:5005/


## Project Local Setup

1. Initiale DB setup
   - Create a SQLServer database named `product.db`.
   - Run the provided SQL scripts to set up the necessary tables and initial data.
   python db-creation.py 
   
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SmartTaskerAI.git
   ```
3. Navigate to the project directory:
   ```bash
   cd SmartTaskerAI
   ```
4. Install the required dependencies:
   - For the frontend:  
     ```bash
     cd frontend
     npm install
     ```            

    - For the backend:  
      ```bash
      cd backend
      pip install -r requirements.txt

      cd product-api 

      venv\Scripts\activate

      pip install -r requirements.txt

      python run.py
      ```
5. Set up the database:
   - Ensure SQLServer is running and accessible.
    - Create a database named `SmartTaskerAI`.
5. Configure environment variables:
   - Create a `.env` file in the backend directory with the following variables:
     ```
     DATABASE_URL=your_database_url
     OPENAI_API_KEY=your_openai_api_key
     ```    
6. Run the backend server:
   ```bash
   cd backend
   flask run
   ```
7. Run the frontend application:
   ```bash
   cd frontend
   ng serve
   ```
8. Open your web browser and navigate to `http://localhost:5005` to access the SmartTaskerAI application.


SmartTaskerAI/
├── LICENSE
├── README.md
└── product-api/
    ├── db-creation.py
    ├── drop-tables.py
    ├── project-setup.py
    ├── requirements.txt
    ├── run.py
    ├── school.db
    ├── tool_debug.log
    ├── app/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── models.py
    │   ├── app_models/
    │   │   └── __init__.py
    │   ├── app_routes/
    │   │   ├── __init__.py
    │   │   ├── chatbot.py
    │   │   └── student.py
    │   └── __pycache__/
    ├── migrations/
    ├── schoolagent/
    │   ├── agentmain.py
    │   ├── apiservice.py
    │   ├── tools.py
    │   └── __pycache__/
    ├── static/
    └── venv/
