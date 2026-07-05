from google.adk.agents import Agent
from tools.business_tools import sales_tool

sales_agent = Agent(
    name="SalesAgent",
    model="gemini-2.5-flash",
    description="Analyzes sales performance.",
    instruction="""
Use sales_tool whenever the user asks about sales,
products or revenue trends.
""",
    tools=[sales_tool],
)