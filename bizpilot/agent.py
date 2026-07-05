from google.adk.agents import Agent

from bizpilot.sub_agents.finance import finance_agent
from bizpilot.sub_agents.sales import sales_agent
from bizpilot.sub_agents.inventory import inventory_agent
from bizpilot.sub_agents.strategy import strategy_agent
from bizpilot.sub_agents.report import report_agent

root_agent = Agent(
    name="BizPilot",
    model="gemini-2.5-flash",
    description="Executive Business Management Agent",
    instruction="""
You are the Executive Orchestrator.

Delegate work to the appropriate specialist agent.

Finance → FinanceAgent

Sales → SalesAgent

Inventory → InventoryAgent

Recommendations → StrategyAgent

Business reports → ReportAgent
""",
    sub_agents=[
        finance_agent,
        sales_agent,
        inventory_agent,
        strategy_agent,
        report_agent,
    ],
)