from google.adk.agents import Agent
from tools.business_tools import finance_tool

finance_agent = Agent(
    name="FinanceAgent",
    model="gemini-2.5-flash",
    description="Analyzes company finances.",
    instruction="""
Use finance_tool to answer questions related to revenue,
expenses, profit and financial performance.
""",
    tools=[finance_tool],
)