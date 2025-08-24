# SmartTaskerAI

## Overview
SmartTaskerAI is an intelligent task management system designed to streamline workflows and enhance productivity using AI-driven insights.

<img width="1878" height="1016" alt="image" src="https://github.com/user-attachments/assets/7d5ec88a-bf23-4385-9ac3-de99067c02f4" />

## Features
- **Unified Pending Task Dashboard:** See and manage all pending tasks in a single, user-friendly view.
- **Smart AI Chatbot:** Get real-time assistance, task suggestions, and answers to queries from a context-aware chatbot powered by Google Gemini AI.
- **Analytics Dashboard:** Gain actionable insights into task progress and productivity via interactive analytics.
- **Student Data Intelligence:** Specialized tools and APIs to fetch and analyze student data, demonstrating practical AI integration for real-world use cases.

## Technology Stack
- **Frontend:** Angular 15+ (separate UI repository)
- **Backend:** Flask (Python)
- **Database:** SQLite (with support for SQL Server)
- **AI/LLM Integration:** Google Gemini AI (Gemini 1.5 Flash model) via LangChain
- **API Documentation**: Swagger/OpenAPI

## AI & Tooling Details

- **Gemini LLM Integration:** The chatbot and assistant features utilize Google Gemini (1.5 Flash) for natural language understanding and smart responses.
- **LangChain Framework:** Employs LangChain for agent-based orchestration, tool invocation, and prompt engineering.
- **Custom Tools:** 
  - **Student Info Tool:** Fetches and delivers detailed student lists and records using database queries.
  - **Web Search Tools:** Integrates DuckDuckGo and Wikipedia search for real-time information retrieval.
- **Memory and Context:** Uses ConversationBufferMemory to maintain chat history and context for more natural, intelligent conversations.

## AI Skills Demonstrated

- **Prompt Engineering:** Custom prompt templates for task and student management.
- **LLM Tool Chaining:** Integration of multiple tools with LLMs for complex, multi-step reasoning.
- **API Design:** End-to-end RESTful API development, including documentation and best practices.
- **Data Handling:** Efficient use of ORM (SQLAlchemy) and database design for scalable data operations.
- **Full Stack Integration:** Orchestrating frontend, backend, database, and AI components into a seamless product.

## System Design
1. **Frontend:** Angular web application (see [UI repo](https://github.com/aks1008/smart-student-management)).
2. **Backend/API:** Flask app exposing REST endpoints, student management, and AI chatbot features.
3. **Database:** Local SQLite (or SQL Server) for persistent data storage.
4. **AI Agent:** Gemini-powered agent with tool-calling capabilities for dynamic task management and Q&A.
5. **API Documentation:** Accessible via Swagger UI at `http://localhost:5005/`.

## Front End UI code GitHub Repo
   ```bash
   git clone https://github.com/aks1008/smart-student-management.git
   ```

## API Documentation
The API documentation is available via Swagger UI at:
http://127.0.0.1:5005/

## Why This Project Stands Out

SmartTaskerAI goes beyond a traditional CRUD app by embedding generative AI and intelligent agents into everyday task management. It demonstrates advanced skills in:

- Modern AI/LLM integration (Google Gemini, LangChain)
- Real-world tool use (search, database agents)
- Full stack and scalable system design
- API-first development and documentation

This project is a testament to practical AI engineering and the ability to build intelligent, production-ready applications.

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

```
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
```

---
**License:** MIT  
**Repository:** [aks1008/SmartTaskerAI](https://github.com/aks1008/SmartTaskerAI)
