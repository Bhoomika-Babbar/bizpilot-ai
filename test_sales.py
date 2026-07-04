from agents.sales_agent import analyze_sales

report = analyze_sales()

print("\n📈 Sales Report")
print("-------------------------")

for key, value in report.items():
    print(f"{key}: {value}")