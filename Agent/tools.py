from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool, tool
from datetime import datetime
import logging
from productservice import get_shopping_list, get_user, get_shopping_list_user

logging.basicConfig(filename='tool_debug.log', level=logging.INFO)

search = DuckDuckGoSearchRun()

search_tool = Tool(
    func=search.run,
    name="DuckDuckGoSearch",
    description="Useful for when you need to answer questions about current events or general knowledge. Input should be a search query.",
)

api_wrapper = WikipediaAPIWrapper(
    top_k_results=5,
    max_length=500,
    max_results=5,
    return_intermediate_steps=True,
    date=datetime.now().strftime("%Y-%m-%d"),
)

wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

@tool("GetProductUserInfo")
def get_product_list_by_user() -> str:
    '''
    You are the assistant helping to answer questions for purchasing. 
    Access the purchase history. Use this tool to get the product list, user list and purchase history. 
    '''
    logging.info(f"Query received for user")

    user_info = get_user()
    shopping_list = get_shopping_list()
    purchases = get_shopping_list_user()

    logging.info(f"User Info: {user_info}")
    logging.info(f"Shopping List: {shopping_list}")
    logging.info(f"Purchase: {purchases}")

    if purchases:
        logging.info(f"yes: {purchases}")
        return purchases  
    else:
        logging.info(f"No: {purchases}")
        return f"No purchases found for."
