from agents.strategy_agent import generate_strategy

recommendations = generate_strategy()

print("\n🎯 Business Recommendations")
print("------------------------------")

for i, recommendation in enumerate(recommendations, start=1):
    print(f"{i}. {recommendation}")