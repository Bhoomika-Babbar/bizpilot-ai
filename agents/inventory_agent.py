from tools.csv_tools import read_csv


def analyze_inventory():
    """
    Analyze inventory levels and identify products that need reordering.
    """

    inventory = read_csv("inventory.csv")

    low_stock = inventory[
        inventory["current_stock"] < inventory["reorder_level"]
    ]

    return {
        "Products to Reorder": low_stock["product"].tolist(),
        "Total Low Stock Items": len(low_stock),
    }