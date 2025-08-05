import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Student Grades Dashboard", layout="wide")

# Data
data = {
    'name': ['lee', 'park', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 88, 99],
    'eng': [91, 89, 99],
    'math': [81, 77, 99],
    'info': [100, 100, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Student Grades Visualization Dashboard")

# Layout with columns
col1, col2 = st.columns(2)

# Grouped Bar Chart
with col1:
    st.subheader("Subject Scores by Student")
    fig_bar = px.bar(
        df,
        x='name',
        y=['kor', 'eng', 'math', 'info'],
        barmode='group',
        title="Individual Subject Scores",
        labels={'name': 'Student', 'value': 'Score', 'variable': 'Subject'}
    )
    fig_bar.update_layout(
        height=400,
        legend_title="Subject",
        yaxis_range=[0, 100]
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Box Plot
with col2:
    st.subheader("Score Distribution by Subject")
    fig_box = px.box(
        df.melt(id_vars=['name'], value_vars=['kor', 'eng', 'math', 'info'],
                var_name='Subject', value_name='Score'),
        x='Subject',
        y='Score',
        title="Score Distribution",
        color='Subject'
    )
    fig_box.update_layout(
        height=400,
        yaxis_range=[0, 100]
    )
    st.plotly_chart(fig_box, use_container_width=True)

# Heatmap
st.subheader("Correlation Heatmap of Subjects")
correlation_matrix = df[['kor', 'eng', 'math', 'info']].corr()
fig_heatmap = px.imshow(
    correlation_matrix,
    text_auto=True,
    title="Subject Score Correlations",
    color_continuous_scale='RdBu_r',
    zmin=-1,
    zmax=1
)
fig_heatmap.update_layout(height=400)
st.plotly_chart(fig_heatmap, use_container_width=True)

# Raw Data Table
st.subheader("Raw Data")
st.dataframe(df.style.format({
    'kor': '{:.0f}',
    'eng': '{:.0f}',
    'math': '{:.0f}',
    'info': '{:.0f}'
}), use_container_width=True)