```python
import streamlit as st
import requests
import pandas as pd

# ---------------------------------------------------
# API BASE URL
# ---------------------------------------------------

API_BASE = "https://breathe-esg-assignment-thoq.onrender.com"

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="ESG Analytics Platform",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🌍 ESG Analytics Dashboard")
st.markdown("### Breathe ESG Internship Assignment")

# ---------------------------------------------------
# FETCH API DATA
# ---------------------------------------------------

try:
    dashboard = requests.get(
        f"{API_BASE}/api/emissions/dashboard/"
    ).json()

    analytics = requests.get(
        f"{API_BASE}/api/emissions/analytics/"
    ).json()

    top_sources = requests.get(
        f"{API_BASE}/api/emissions/top-sources/"
    ).json()

except Exception as e:
    st.error(f"API Connection Error: {e}")
    st.stop()

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Emissions",
        dashboard.get("total_emissions", "0")
    )

with col2:
    st.metric(
        "Active Companies",
        dashboard.get("companies", "0")
    )

with col3:
    st.metric(
        "Audit Records",
        dashboard.get("audits", "0")
    )

st.divider()

# ---------------------------------------------------
# ANALYTICS SECTION
# ---------------------------------------------------

st.subheader("📊 Emission Analytics")

try:

    # Convert dict → dataframe safely
    if isinstance(analytics, dict):
        analytics_df = pd.DataFrame(
            list(analytics.items()),
            columns=["Metric", "Value"]
        )

    elif isinstance(analytics, list):
        analytics_df = pd.DataFrame(analytics)

    else:
        analytics_df = pd.DataFrame()

    if not analytics_df.empty:
        st.dataframe(analytics_df)

        # Show chart only for numeric values
        numeric_df = analytics_df.select_dtypes(include=['number'])

        if not numeric_df.empty:
            st.bar_chart(numeric_df)

    else:
        st.warning("No analytics data available")

except Exception as e:
    st.error(f"Analytics Error: {e}")

# ---------------------------------------------------
# TOP SOURCES
# ---------------------------------------------------

st.subheader("🏭 Top Emission Sources")

try:

    if isinstance(top_sources, dict):
        top_df = pd.DataFrame(
            list(top_sources.items()),
            columns=["Source", "Value"]
        )

    elif isinstance(top_sources, list):
        top_df = pd.DataFrame(top_sources)

    else:
        top_df = pd.DataFrame()

    if not top_df.empty:
        st.dataframe(top_df)

    else:
        st.warning("No top source data available")

except Exception as e:
    st.error(f"Top Sources Error: {e}")

# ---------------------------------------------------
# PDF REPORT
# ---------------------------------------------------

st.subheader("📄 ESG Report")

pdf_url = f"{API_BASE}/api/emissions/pdf-report/"

st.markdown(
    f"[Download ESG PDF Report]({pdf_url})"
)

# ---------------------------------------------------
# SYSTEM STATUS
# ---------------------------------------------------

st.divider()

st.success("🚀 ESG Analytics Platform Live")

st.info(
    "Backend APIs connected successfully."
)
```
