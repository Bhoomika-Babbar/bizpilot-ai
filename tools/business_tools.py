from agents.finance_agent import analyze_finances
from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory
from agents.strategy_agent import generate_strategy
from agents.report_agent import generate_report


def finance_tool():
    """Returns finance analysis."""
    return analyze_finances()


def sales_tool():
    """Returns sales analysis."""
    return analyze_sales()


def inventory_tool():
    """Returns inventory analysis."""
    return analyze_inventory()


def strategy_tool():
    """Returns business recommendations."""
    return generate_strategy()


def report_tool():
    """Returns executive report."""
    return generate_report()