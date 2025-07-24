from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wikipedia_tool, get_product_list_by_user 

#load environment variables
load_dotenv()

# Costumize output resopnse
class ResponseModel(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Create parser for the response model, i.e. from LLM to customize model to use in our program
parser = PydanticOutputParser(pydantic_object=ResponseModel)

#input template for the LLM
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
        For any purchase-related question, always use the get_product_list_by_user tool.
        The tool returns a list of purchases as structured data (list of dictionaries with item_name, amount, date).
        You can use this data to answer follow-up questions, such as the price, or date of a specific item, or to summarize the user's purchase history.
        If the user asks about a specific detail (e.g., price of an item), extract it from the tool's output and include it in your response.
 
        """),
        ("human","{query}"),
        ("placeholder","{chat_history}"),
        ("placeholder","{agent_scratchpad}"),
    ]
)

geminiLLM = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    max_tokens=500
)

tools = [get_product_list_by_user, search_tool, wikipedia_tool]

agent = create_tool_calling_agent(
    llm=geminiLLM,
    prompt=prompt,
    tools=tools
    )

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True
)

chat_history = []

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break

    response = agent_executor.invoke({
        "query": query,
        "chat_history": chat_history
    })
    #print("Agent:", response)

    # Add user and agent messages to chat_history
    chat_history.append({"role": "user", "content": query})
    chat_history.append({"role": "assistant", "content": str(response)})

    # If the response contains a purchase list, add it as a fact for future turns
    # (Assuming your response is a dict and has a 'summary' or similar field)
    if isinstance(response, dict) and "summary" in response:
        # If summary is a list (structured data), serialize it
        if isinstance(response["summary"], list):
            chat_history.append({
                "role": "system",
                "content": f"FACT: Previous purchase data: {json.dumps(response['summary'])}"
            })
        else:
            chat_history.append({
                "role": "system",
                "content": f"FACT: {response['summary']}"
            })