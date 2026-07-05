from google.adk.agents import Agent
from tools.business_tools import report_tool

report_agent = Agent(
    name="ReportAgent",
    model="gemini-2.5-flash",
    description="Executive reporting agent.",
    instruction="""
Always use report_tool when asked for
a complete business report.
""",
    tools=[report_tool],
)