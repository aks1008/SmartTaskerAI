from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool, tool  
from datetime import datetime
import logging 
from schoolagent.apiservice import get_student_list as api_get_student_list

logging.basicConfig(filename='tool_debug.log', level=logging.INFO)

search = DuckDuckGoSearchRun()

# Tool 1: DuckDuckGoSearch
search_tool = Tool(
    func=search.run,
    name="DuckDuckGoSearch",
    description="Useful for when you need to answer questions about current events or general knowledge. Input should be a search query.",
)

# Tool 2: Wikipedia
api_wrapper = WikipediaAPIWrapper(
    top_k_results=5,
    max_length=500,
    max_results=5,
    return_intermediate_steps=True,
    date=datetime.now().strftime("%Y-%m-%d"),
)

wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Tool 3: GetStudentList
@tool("GetStudentList")
def get_student_list() -> str:
    '''
    You are the assistant helping to answer questions for school information. 
    Access the student list. Use this tool to get the student list and their details.
    '''
    logging.info(f"Query received for student list")

    student_list = api_get_student_list()

    logging.info(f"Student List: {student_list}")

    if student_list:
        logging.info(f"yes: {student_list}")
        return student_list
    else:
        logging.info(f"No: {student_list}")
        return f"No students found."
