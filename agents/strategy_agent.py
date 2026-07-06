from agents.finance_agent import analyze_finances
from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory


def generate_strategy(sales_df=None, expenses_df=None, inventory_df=None):
    """
    Generate AI business recommendations.
    Uses uploaded data if provided.
    """

    finance = analyze_finances(sales_df, expenses_df)
    sales = analyze_sales(sales_df)
    inventory = analyze_inventory(inventory_df)

    recommendations = []

    if finance["Profit"] < 50000:
        recommendations.append(
            "Review operating expenses to improve profitability."
        )

    if inventory["Total Low Stock Items"] > 0:
        recommendations.append(
            f"Restock: {', '.join(inventory['Products to Reorder'])}."
        )

    recommendations.append(
        f"Increase promotion of {sales['Best Selling Product']}."
    )

    recommendations.append(
        f"Review pricing or marketing strategy for {sales['Worst Selling Product']}."
    )

    return recommendations