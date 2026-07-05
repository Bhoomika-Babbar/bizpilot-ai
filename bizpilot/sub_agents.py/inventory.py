from google.adk.agents import Agent
from tools.business_tools import inventory_tool

inventory_agent = Agent(
    name="InventoryAgent",
    model="gemini-2.5-flash",
    description="Monitors inventory.",
    instruction="""
Use inventory_tool whenever inventory,
stock or reorder questions are asked.
""",
    tools=[inventory_tool],
)