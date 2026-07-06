import pandas as pd
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import streamlit as st
import plotly.express as px

from agents.finance_agent import analyze_finances
from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory
from agents.strategy_agent import generate_strategy
from agents.report_agent import generate_report

from tools.csv_tools import read_csv

st.set_page_config(
    page_title="BizPilot AI",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

[data-testid="stMetric"]{
    background:#1b263b;
    padding:18px;
    border-radius:15px;
    border:1px solid #2d3e50;
    box-shadow:0px 4px 15px rgba(0,0,0,.25);
}

[data-testid="stMetricValue"]{
    font-size:34px;
    font-weight:bold;
}

[data-testid="stMetricLabel"]{
    font-size:17px;
}

h1{
    color:#00D084;
}

h2{
    color:white;
}

h3{
    color:#00D084;
}

</style>
""", unsafe_allow_html=True)

logo_path = ROOT / "assets" / "logo.png"

# ---------------- Sidebar ----------------

with st.sidebar:
    st.image(str(logo_path), width=90)
    st.markdown("# 🚀 BizPilot AI")
    st.caption("AI Business Intelligence")
    st.markdown("---")

    st.sidebar.subheader("📂 Upload Business Data")

    sales_file = st.sidebar.file_uploader(
        "Sales CSV",
        type=["csv"],
    )

    expenses_file = st.sidebar.file_uploader(
        "Expenses CSV",
        type=["csv"],
    )

    inventory_file = st.sidebar.file_uploader(
        "Inventory CSV",
        type=["csv"],
    )

    st.sidebar.markdown("---")

    with st.sidebar.expander("📋 Expected CSV Format"):

        st.markdown("""
    ### Sales CSV
    - product
    - units_sold
    - revenue

    ### Expenses CSV
    - category
    - amount

    ### Inventory CSV
    - product
    - current_stock
    - reorder_level
    """)


page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Finance",
        "Sales",
        "Inventory",
        "Recommendations",
        "AI Assistant",
        "Executive Report",
    ],
)


# ---------------- Load Business Data ----------------

using_uploaded_data = any([
    sales_file,
    expenses_file,
    inventory_file
])

if using_uploaded_data:
    st.sidebar.success("✅ Using uploaded business data")
else:
    st.sidebar.info("📄 Using sample demo dataset")


if sales_file:
    sales_df = pd.read_csv(sales_file)
else:
    sales_df = read_csv("sales.csv")

if expenses_file:
    expenses_df = pd.read_csv(expenses_file)
else:
    expenses_df = read_csv("expenses.csv")

if inventory_file:
    inventory_df = pd.read_csv(inventory_file)
else:
    inventory_df = read_csv("inventory.csv")

finance = analyze_finances(sales_df,expenses_df)
sales = analyze_sales(sales_df)
inventory = analyze_inventory(inventory_df)

# ---------------- Dashboard ----------------

if page == "Dashboard":

    col1, col2 = st.columns([1,5])

    with col1:
        st.image(str(logo_path), width=120)

    with col2:
        st.title("BizPilot AI")
        st.caption("Executive Business Intelligence Dashboard")

    st.success(
        "👋 Welcome to BizPilot AI! Analyze your business performance using AI-powered business agents."
    )

    st.subheader("📊 Business Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            label="💰 Total Revenue",
            value=f"₹{finance['Total Revenue']:,}",
            delta="▲ 12%"
        )

    with c2:
        st.metric(
            label="💸 Total Expenses",
            value=f"₹{finance['Total Expenses']:,}",
            delta="▼ 5%"
        )

    with c3:
        st.metric(
            label="📈 Net Profit",
            value=f"₹{finance['Profit']:,}",
            delta="▲ 18%"
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        finance_chart = px.bar(
            x=["Revenue","Expenses","Profit"],
            y=[
                finance["Total Revenue"],
                finance["Total Expenses"],
                finance["Profit"]
            ],
            color=["Revenue","Expenses","Profit"],
            title="Financial Performance",
            text_auto=True,
        )

        finance_chart.update_layout(
            template="plotly_dark",
            height=420,
            showlegend=False,
        )

        st.plotly_chart(finance_chart, use_container_width=True)

    with right:

        sales_chart = px.bar(
            sales_df,
                x="product",
                y="units_sold",
                color="product",
                text_auto=True,
                title="Product Sales",
        )

        sales_chart.update_layout(
                template="plotly_dark",
                height=420,
        )

        st.plotly_chart(sales_chart, use_container_width=True)
                
    st.divider()

    st.subheader("📊 Revenue Distribution")

    fig3 = px.pie(
    sales_df,
    values="revenue",
    names="product",
    hole=.65,
    title="Revenue Distribution",
    )

    fig3.update_traces(
        textposition="inside",
        textinfo="percent+label",
    )

    fig3.update_layout(
        template="plotly_dark",
        height=500,
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    st.subheader("🤖 AI Executive Summary")

    if st.button("✨ Generate AI Business Summary"):

        summary = f"""
    ### 📊 Business Health

    ✅ Revenue: ₹{finance['Total Revenue']:,}

    ✅ Expenses: ₹{finance['Total Expenses']:,}

    ✅ Profit: ₹{finance['Profit']:,}

    🏆 Best Selling Product:
    {sales['Best Selling Product']}

    📉 Lowest Selling Product:
    {sales['Worst Selling Product']}

    📦 Products to Restock:
    {", ".join(inventory["Products to Reorder"])}

    ### 💡 AI Recommendations

    """

        for item in generate_strategy(sales_df,expenses_df,inventory_df):
            summary += f"• {item}\n"

        st.success(summary)

    st.divider()

    st.subheader("🤖 AI Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"🏆 Best Selling Product: **{sales['Best Selling Product']}**")

        st.success(f"💰 Profit: ₹{finance['Profit']:,}")

    with col2:
        st.warning(
            "📦 Products to Restock:\n\n"
            + ", ".join(inventory["Products to Reorder"])
        )

        st.error(f"📉 Lowest Seller: {sales['Worst Selling Product']}")

# ---------------- Finance ----------------

elif page == "Finance":

    st.title("💰 Financial Summary")

    st.metric("Revenue", f"₹{finance['Total Revenue']:,}")
    st.metric("Expenses", f"₹{finance['Total Expenses']:,}")
    st.metric("Profit", f"₹{finance['Profit']:,}")

# ---------------- Sales ----------------

elif page == "Sales":

    st.title("📈 Sales Analysis")

    c1, c2, c3 = st.columns(3)

    c1.metric("🏆 Best Seller", sales["Best Selling Product"])
    c2.metric("📉 Lowest Seller", sales["Worst Selling Product"])
    c3.metric("📦 Avg Units", sales["Average Units Sold"])

# ---------------- Inventory ----------------

elif page == "Inventory":

    st.title("📦 Inventory")

    if inventory["Products to Reorder"]:

        st.subheader("Products to Restock")

        st.dataframe(
            inventory_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success("Inventory looks healthy!")

# ---------------- Strategy ----------------

elif page == "Recommendations":

    st.title("🧠 AI Business Recommendations")

    for i, item in enumerate(generate_strategy(sales_df,expenses_df,inventory_df,), 1):
        st.success(f"{i}. {item}")
# ---------------- AI Assistant ----------------

elif page == "AI Assistant":

    st.title("🤖 BizPilot AI Assistant")
    st.write("Ask anything about your business.")

    question = st.chat_input("Ask a business question...")

    if question:

        st.chat_message("user").write(question)

        q = question.lower()

        if "profit" in q:

            answer = f"""
### 💰 Profit Analysis

Current Profit: **₹{finance['Profit']:,}**

Your business is currently profitable.

Recommendation:
- Increase sales of high-margin products.
- Continue controlling operating expenses.
"""

        elif "revenue" in q:

            answer = f"""
### 📈 Revenue

Current Revenue is **₹{finance['Total Revenue']:,}**.
"""

        elif "expense" in q:

            answer = f"""
### 💸 Expenses

Current Expenses are **₹{finance['Total Expenses']:,}**.
"""

        elif "best" in q:

            answer = f"""
🏆 Best Selling Product

**{sales['Best Selling Product']}**

This product is performing the best.
"""

        elif "worst" in q:

            answer = f"""
📉 Lowest Selling Product

**{sales['Worst Selling Product']}**

Consider improving marketing or pricing.
"""

        elif "inventory" in q or "stock" in q:

            answer = "📦 Products to Restock:\n\n"

            for product in inventory["Products to Reorder"]:
                answer += f"- {product}\n"

        elif "recommend" in q:

            answer = "### 🤖 AI Recommendations\n\n"

            for item in generate_strategy(sales_df,expenses_df,inventory_df):
                answer += f"✅ {item}\n\n"

        else:

            answer = """
I can answer questions about:

• Profit
• Revenue
• Expenses
• Inventory
• Best selling products
• Recommendations
"""

        st.chat_message("assistant").write(answer)

# ---------------- Report ----------------

else:

    st.title("📄 Executive Report")

    report = generate_report(sales_df,expenses_df,inventory_df)

    st.code(report, language="text")

    st.download_button(
        "📥 Download Report",
        report,
        file_name="BizPilot_Report.txt",
    )

    st.divider()

    st.caption(
        "© 2026 BizPilot AI • Built with Streamlit, Plotly, Python & Google ADK"
    )