import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the financial data
data = {
    "Company": ["Apple", "Tesla", "Microsoft"],
    "Year": [2024, 2024, 2024],
    "Total Revenue": [394.3, 96.8, 232.4],  # in billions
    "Net Income Change": ["increased by 5.3%", "decreased by 2.1%", "increased by 3.6%"]
}
df = pd.DataFrame(data)

# Step 2: Define chatbot logic
def respond_to_query(query):
    query = query.lower()

    if "total revenue" in query:
        responses = [
            f"{row['Company']}'s total revenue in {row['Year']} was ${row['Total Revenue']} billion."
            for _, row in df.iterrows()
        ]
        return "\n".join(responses)

    elif "net income" in query:
        responses = [
            f"{row['Company']}'s net income has {row['Net Income Change']} in {row['Year']}."
            for _, row in df.iterrows()
        ]
        return "\n".join(responses)

    elif "graph" in query or "visual" in query:
        return "graph"

    elif "help" in query:
        return ("You can ask:\n"
                "- What is the total revenue?\n"
                "- How has net income changed over the last year?\n"
                "- Show revenue graph\n"
                "- Show net income change graph")

    else:
        return "Sorry, I can only provide information on predefined queries."

# Step 3: Define Streamlit app layout
st.set_page_config(page_title="Financial Chatbot", layout="centered")

st.title("📊 Financial Insights Chatbot")
user_input = st.text_input("Ask me about company revenue, net income, or graphs:")

if user_input:
    response = respond_to_query(user_input)

    if response == "graph":
        if "revenue" in user_input:
            st.subheader("📈 Revenue Comparison (2024)")
            fig, ax = plt.subplots()
            ax.bar(df["Company"], df["Total Revenue"], color=["green", "blue", "purple"])
            ax.set_ylabel("Revenue (in Billion $)")
            ax.set_title("Total Revenue of Companies - 2024")
            st.pyplot(fig)

        elif "net income" in user_input:
            st.subheader("📈 Net Income Change (2024)")
            changes = [5.3, -2.1, 3.6]
            fig, ax = plt.subplots()
            ax.bar(df["Company"], changes, color=["green" if c > 0 else "red" for c in changes])
            ax.set_ylabel("Net Income Change (%)")
            ax.set_title("Net Income Change of Companies - 2024")
            st.pyplot(fig)
        else:
            st.write("Please specify if you want the revenue or net income graph.")
    else:
        st.text_area("Response", value=response, height=200)

st.markdown("---")
st.info("Try: 'What is the total revenue?', 'net income', or 'Show revenue graph'")
