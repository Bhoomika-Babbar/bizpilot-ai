from tools.csv_tools import read_csv


def analyze_finances():
    """
    Reads sales and expense data and returns a financial summary.
    """

    sales = read_csv("sales.csv")
    expenses = read_csv("expenses.csv")

    total_revenue = int(sales["revenue"].sum())
    total_expenses = int(expenses["amount"].sum())
    profit = int(total_revenue - total_expenses)

    return {
        "Total Revenue": total_revenue,
        "Total Expenses": total_expenses,
        "Profit": profit,
    }