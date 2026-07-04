from agents.finance_agent import analyze_finances
from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory
from agents.strategy_agent import generate_strategy


def generate_report():
    finance = analyze_finances()
    sales = analyze_sales()
    inventory = analyze_inventory()
    strategy = generate_strategy()

    report = f"""
==============================
      BizPilot AI Report
==============================

FINANCIAL SUMMARY
-----------------
Total Revenue : ₹{finance['Total Revenue']:,}
Total Expenses: ₹{finance['Total Expenses']:,}
Profit         : ₹{finance['Profit']:,}

SALES SUMMARY
-------------
Best Selling Product : {sales['Best Selling Product']}
Worst Selling Product: {sales['Worst Selling Product']}
Average Units Sold   : {sales['Average Units Sold']}

INVENTORY
---------
Products to Reorder:
{", ".join(inventory["Products to Reorder"])}

RECOMMENDATIONS
---------------
"""

    for i, item in enumerate(strategy, 1):
        report += f"{i}. {item}\n"

    return report