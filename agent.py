import os
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent, create_openai_tools_agent, create_structured_chat_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI


OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "http://127.0.0.1:8000/v1")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "EMPTY")

tools = [TavilySearchResults(max_results=1)]
# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")

llm = ChatOpenAI(openai_api_base=OPENAI_BASE_URL , openai_api_key=OPENAI_API_KEY)

# Construct the OpenAI Functions agent
agent1 = create_openai_functions_agent(llm, tools, prompt)
agent_executor1 = AgentExecutor(agent=agent1, tools=tools, verbose=True)
output1 = agent_executor1.invoke({"input": "what is LangChain?"})["output"]
print(output1)


# Construct the OpenAI Tools agent
agent2 = create_openai_tools_agent(llm, tools, prompt)
agent_executor2 = AgentExecutor(agent=agent2, tools=tools, verbose=True)
output2 = agent_executor2.invoke({"input": "what is LangChain?"})["output"]
print(output2)