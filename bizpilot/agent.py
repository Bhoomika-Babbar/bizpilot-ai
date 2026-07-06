from google.adk.agents import Agent

from tools.business_tools import (
    finance_tool,
    sales_tool,
    inventory_tool,
    strategy_tool,
    report_tool,
)

root_agent = Agent(
    name="BizPilot",
    model="gemini-2.5-flash",
    description="AI-powered Multi-Agent Business Intelligence Assistant built using Google ADK.",
    instruction="""
You are BizPilot AI.

You help business owners understand and manage their business.

Use the appropriate tool based on the user's request.

Finance questions -> finance_tool
Sales questions -> sales_tool
Inventory questions -> inventory_tool
Business recommendations -> strategy_tool
Complete business reports -> report_tool

Always use the tools. Never make up business data.
""",
    tools=[
        finance_tool,
        sales_tool,
        inventory_tool,
        strategy_tool,
        report_tool,
    ],
)