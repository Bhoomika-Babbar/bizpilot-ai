from agents.finance_agent import analyze_finances
from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory
from agents.strategy_agent import generate_strategy


def generate_report(sales_df=None, expenses_df=None, inventory_df=None):
    """
    Generate an executive business report.
    Uses uploaded data if provided.
    """

    finance = analyze_finances(sales_df, expenses_df)
    sales = analyze_sales(sales_df)
    inventory = analyze_inventory(inventory_df)
    strategy = generate_strategy(
        sales_df,
        expenses_df,
        inventory_df,
    )

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