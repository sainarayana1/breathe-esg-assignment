python
import streamlit as st
import requests
import pandas as pd

API_BASE = "https://breathe-esg-assignment-thoq.onrender.com"

st.set_page_config(
    page_title="ESG Analytics Platform",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 ESG Analytics Dashboard")
st.write("Breathe ESG Internship Assignment")

# ---------------------------------------------------
# FETCH DATA
# ---------------------------------------------------

dashboard = {}
analytics = {}
top_sources = {}

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
    st.error(f"API Error: {e}")

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Emissions",
        dashboard.get("total_emissions", 0)
    )

with col2:
    st.metric(
        "Active Companies",
        dashboard.get("companies", 0)
    )

with col3:
    st.metric(
        "Audit Records",
        dashboard.get("audits", 0)
    )

st.divider()

# ---------------------------------------------------
# ANALYTICS
# ---------------------------------------------------

st.subheader("📊 Emission Analytics")

try:

    if isinstance(analytics, dict):

        analytics_df = pd.DataFrame(
            [analytics]
        )

    elif isinstance(analytics, list):

        analytics_df = pd.DataFrame(
            analytics
        )

    else:

        analytics_df = pd.DataFrame()

    st.dataframe(analytics_df)

except Exception as e:

    st.error(f"Analytics Error: {e}")

# ---------------------------------------------------
# TOP SOURCES
# ---------------------------------------------------

st.subheader("🏭 Top Emission Sources")

try:

    if isinstance(top_sources, dict):

        top_df = pd.DataFrame(
            [top_sources]
        )

    elif isinstance(top_sources, list):

        top_df = pd.DataFrame(
            top_sources
        )

    else:

        top_df = pd.DataFrame()

    st.dataframe(top_df)

except Exception as e:

    st.error(f"Top Sources Error: {e}")

# ---------------------------------------------------
# PDF REPORT
# ---------------------------------------------------

st.subheader("📄 ESG Report")

st.markdown(
    f"[Download PDF Report]({API_BASE}/api/emissions/pdf-report/)"
)

st.divider()

st.success("🚀 ESG Analytics Platform Live")

