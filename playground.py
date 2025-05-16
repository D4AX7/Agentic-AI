from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
import phi.api      
import os
from dotenv import load_dotenv
from phi.playground import Playground,serve_playground_app

load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

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

app = Playground(
    agents=[web_search_agent, financial_agent]
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)

