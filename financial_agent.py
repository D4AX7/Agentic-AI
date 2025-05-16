from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo



web_search_agent =Agent(
    name="Web Search Agent",
    role="search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source of the information you find."],
    show_tools_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="Financial Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True, company_news=True)],
    instructions=["Use table to display the data."],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["You are a team of agents.,Always include the source of the information you find.,use table to display the data."],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations for NVDIA stock and find the latest news about it.",stream=True)
