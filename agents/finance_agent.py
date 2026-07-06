from tools.csv_tools import read_csv


def analyze_finances(sales_df=None, expenses_df=None):
    """
    Returns a financial summary.
    Uses uploaded data if provided, otherwise reads the default CSV files.
    """

    if sales_df is None:
        sales_df = read_csv("sales.csv")

    if expenses_df is None:
        expenses_df = read_csv("expenses.csv")

    total_revenue = int(sales_df["revenue"].sum())
    total_expenses = int(expenses_df["amount"].sum())
    profit = total_revenue - total_expenses

    return {
        "Total Revenue": total_revenue,
        "Total Expenses": total_expenses,
        "Profit": profit,
    }