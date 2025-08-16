# SmartTaskerAI

## Overview
SmartTaskerAI is an intelligent task management system designed to streamline workflows and enhance productivity using AI-driven insights.

## Features
1. **Dashboard for Pending Task List**: View and manage all your pending tasks in one place.
2. **Smart Chat Bot to Assist Tasks**: Get real-time assistance and task suggestions from an AI-powered chatbot.
3. **Insightful Dashboard**: Gain actionable insights into your tasks and productivity through a comprehensive analytics dashboard.

## System Design
1. Web APP developed using Angular for the frontend and Flask for the backend.
2. Utilizes a SQLServer database for data storage and management.
3. Integrates with OpenAI's GPT-3.5 for AI-driven task management and insights.
4. Implements a RESTful API for seamless communication between the frontend and backend.
5. Model Context Protocol (MCP) for efficient data handling and processing.

<img width="1878" height="1016" alt="image" src="https://github.com/user-attachments/assets/7d5ec88a-bf23-4385-9ac3-de99067c02f4" />


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
8. Open your web browser and navigate to `http://localhost:4200` to access the SmartTaskerAI application.


cd product-api 

venv\Scripts\activate

pip install -r requirements.txt

python run.py
