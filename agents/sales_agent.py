from tools.csv_tools import read_csv


def analyze_sales(sales_df=None):
    """
    Analyze sales performance.
    Uses uploaded data if provided, otherwise reads the default CSV.
    """

    if sales_df is None:
        sales_df = read_csv("sales.csv")

    total_revenue = int(sales_df["revenue"].sum())

    best_product = sales_df.loc[sales_df["units_sold"].idxmax()]

    worst_product = sales_df.loc[sales_df["units_sold"].idxmin()]

    average_units = float(sales_df["units_sold"].mean())

    return {
        "Total Revenue": total_revenue,
        "Best Selling Product": str(best_product["product"]),
        "Worst Selling Product": str(worst_product["product"]),
        "Average Units Sold": round(average_units, 2),
    }