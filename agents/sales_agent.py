from tools.csv_tools import read_csv


def analyze_sales():
    """
    Analyze sales performance.
    """

    sales = read_csv("sales.csv")

    total_revenue = int(sales["revenue"].sum())

    best_product = sales.loc[sales["units_sold"].idxmax()]

    worst_product = sales.loc[sales["units_sold"].idxmin()]

    average_units = float(sales["units_sold"].mean())

    return {
        "Total Revenue": total_revenue,
        "Best Selling Product": str(best_product["product"]),
        "Worst Selling Product": str(worst_product["product"]),
        "Average Units Sold": round(average_units, 2),
    }