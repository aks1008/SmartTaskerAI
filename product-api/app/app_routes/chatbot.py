from flask import request
from schoolagent.agentmain import chatbotquery
from flask_restx import Namespace, Resource, fields
from typing import Dict, Any

chatbot_ns = Namespace('chatbot', description='Chatbot related operations')

chatbot_input = chatbot_ns.model("ChatbotInput", {
    "query": fields.String(required=True, description="User query for chatbot")
})

@chatbot_ns.route('/')
class ChatbotResource(Resource):
    @chatbot_ns.expect(chatbot_input)
    @chatbot_ns.doc(description="Submit a query to the chatbot")
    def post(self) -> Dict[str, Any]:
        """
        Handle chatbot queries.
        Expects JSON payload: { "query": "your question here" }
        """
        if not request.is_json:
            return {"error": "Request must be JSON"}, 400

        data = request.get_json()
        query = data.get("query")

        if not query or not isinstance(query, str):
            return {"error": "Missing or invalid 'query' field"}, 400
        
        if query.lower() in ["exit", "quit", "end"]:
            return {"message": "Goodbye!"}, 200

        response = chatbotquery(query)
        return response, 200
   