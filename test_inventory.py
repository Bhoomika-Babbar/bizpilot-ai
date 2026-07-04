from agents.inventory_agent import analyze_inventory

report = analyze_inventory()

print("\n📦 Inventory Report")
print("----------------------------")

for key, value in report.items():
    print(f"{key}: {value}")