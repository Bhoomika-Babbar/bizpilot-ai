from agents.finance_agent import analyze_finances

report = analyze_finances()

print("\n📊 Finance Report")
print("------------------------")

for key, value in report.items():
    print(f"{key}: ₹{value:,}")