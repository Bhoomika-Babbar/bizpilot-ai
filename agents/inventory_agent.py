from tools.csv_tools import read_csv


def analyze_inventory(inventory_df=None):
    """
    Analyze inventory levels and identify products that need reordering.
    Uses uploaded data if provided, otherwise reads the default CSV.
    """

    if inventory_df is None:
        inventory_df = read_csv("inventory.csv")

    low_stock = inventory_df[
        inventory_df["current_stock"] < inventory_df["reorder_level"]
    ]

    return {
        "Products to Reorder": [str(p) for p in low_stock["product"].tolist()],
        "Total Low Stock Items": int(len(low_stock)),
    }