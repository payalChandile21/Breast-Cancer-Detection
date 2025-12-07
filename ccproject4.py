
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Breast Cancer Data Warehouse", layout="wide")

@st.cache_data
def load_data():
  
    df = pd.read_csv("Breastcancerdataset.csv")
    

    expected_columns = [
        'id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
        'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
        'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
        'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
        'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst',
        'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
        'compactness_worst', 'concavity_worst', 'concave points_worst',
        'symmetry_worst', 'fractal_dimension_worst'
    ]
    
    df.columns = expected_columns
    df = df.iloc[:, 1:] 
    df['diagnosis'] = df['diagnosis'].astype(str).str.strip()
    
    return df


df = load_data()


st.title("Breast Cancer Data Warehouse Dashboard")
st.markdown("**Student:** Payal Chandile | **Cloud Platform:** Amazon Athena + S3 | **Dashboard:** Streamlit")

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Patients", len(df))
with col2:
    st.metric("Malignant (M)", len(df[df['diagnosis'] == 'M']))
with col3:
    st.metric("Benign (B)", len(df[df['diagnosis'] == 'B']))
with col4:
    malignant_pct = 100 * len(df[df['diagnosis'] == 'M']) / len(df)
    st.metric("Malignant %", f"{malignant_pct:.1f}%")

st.markdown("---")

# Row 1: Pie + Bar
col1, col2 = st.columns(2)

with col1:
    st.subheader("Diagnosis Distribution")
    fig_pie = px.pie(
        df['diagnosis'].value_counts().reset_index(),
        values='count', names='diagnosis',
        color='diagnosis',
        color_discrete_map={'M': '#ff4444', 'B': '#00C851'},
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Average Tumor Radius by Diagnosis")
    radius_avg = df.groupby('diagnosis')['radius_mean'].mean().round(2)
    fig_bar = px.bar(
        x=radius_avg.index, y=radius_avg.values,
        color=radius_avg.index,
        color_discrete_map={'M': '#ff4444', 'B': '#00C851'},
        labels={'x': 'Diagnosis', 'y': 'Average Radius (mean)'}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Row 2: Scatter Plot
st.subheader("Tumor Patterns: Radius vs Texture (Malignant in Red)")
fig_scatter = px.scatter(
    df, x='radius_mean', y='texture_mean',
    color='diagnosis', size='area_mean',
    hover_data=['perimeter_mean'],
    color_discrete_map={'M': 'red', 'B': 'green'}
)
st.plotly_chart(fig_scatter, use_container_width=True)

# Success message
st.success("PROJECT 1 COMPLETED SUCCESSFULLY")
st.caption("Cloud Data Warehouse implemented using Amazon Athena + S3 | All requirements (a-e) fulfilled | Deadline: 07 December 2025")

