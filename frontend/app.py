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
st.markdown("### Breathe ESG Internship Assignment")

# ----------------------------------------------------
# DASHBOARD API
# ----------------------------------------------------

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

# ----------------------------------------------------
# KPI CARDS
# ----------------------------------------------------

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

# ----------------------------------------------------
# ANALYTICS SECTION
# ----------------------------------------------------

st.subheader("📊 Emission Analytics")

analytics_df = pd.DataFrame(analytics)

if not analytics_df.empty:
    st.bar_chart(analytics_df)
else:
    st.warning("No analytics data available")

# ----------------------------------------------------
# TOP SOURCES
# ----------------------------------------------------

st.subheader("🏭 Top Emission Sources")

top_df = pd.DataFrame(top_sources)

if not top_df.empty:
    st.dataframe(top_df)
else:
    st.warning("No top sources available")

# ----------------------------------------------------
# PDF REPORT
# ----------------------------------------------------

st.subheader("📄 Generate ESG Report")

pdf_url = f"{API_BASE}/api/emissions/pdf-report/"

st.markdown(
    f"[Download ESG PDF Report]({pdf_url})"
)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.divider()

st.success("🚀 ESG Analytics Platform Live")