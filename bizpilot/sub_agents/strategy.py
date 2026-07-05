from google.adk.agents import Agent
from tools.business_tools import strategy_tool

strategy_agent = Agent(
    name="StrategyAgent",
    model="gemini-2.5-flash",
    description="Business advisor.",
    instruction="""
Use strategy_tool to generate recommendations.
""",
    tools=[strategy_tool],
)