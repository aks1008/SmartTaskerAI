from dotenv import load_dotenv
from flask import jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from schoolagent.tools import search_tool, wikipedia_tool, get_student_list 
from langchain_core.messages import HumanMessage, AIMessage

#load environment variables
load_dotenv()

#input template for the LLM
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
        You are a helpful assistant.
        For any student-related question, always use the get_student_list tool.
        The tool returns a list of students as structured data (list of dictionaries with name, studentid, totalmarks, emergencycontact, dateofbirth, classname, etc.).
        You can use this data to answer follow-up questions, such as the total marks, or class name of a specific student, or to summarize the student's information.
        If the user asks about a specific detail (e.g., total marks of a student), extract it from the tool's output and include it in your response.
        """),
        ("placeholder","{chat_history}"),
        ("human","{query}"),
        ("placeholder","{agent_scratchpad}"),
    ]
)

geminiLLM = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    max_tokens=500
)

tools = [get_student_list, search_tool, wikipedia_tool]

agent = create_tool_calling_agent(
    llm=geminiLLM,
    prompt=prompt,
    tools=tools
    )

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True,
    memory=memory
)

def serialize_message(msg):
    if isinstance(msg, HumanMessage) or isinstance(msg, AIMessage):
        return {
            "type": msg.__class__.__name__,
            "content": msg.content
        }
    return str(msg)  # fallback for unknown types

def chatbotquery(query):
    '''
    take query as input and provide output
    '''
    if query.lower() in ["exit", "quit", "end"]:
        return

    # The AgentExecutor with memory handles history automatically.
    # We only need to pass the input variable 'query'.
    response = agent_executor.invoke({"query": query})
    print("Full resopnse",response)
    print("Agent:", response['output'])
    
    #return ({"response": response})

    # Serialize chat history
    chat_history = response.get("chat_history", [])
    serialized_history = [serialize_message(msg) for msg in chat_history]

    # Serialize intermediate steps if needed
    intermediate_steps = response.get("intermediate_steps", [])
    serialized_steps = [str(step) for step in intermediate_steps]

    return {
        "query": query,
        "output": response.get("output"),
        "chat_history": serialized_history,
        "intermediate_steps": serialized_steps
    }

