import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Attrition Dashboard", layout="wide")

# Load data and model
@st.cache_data
def load_data():
    return pd.read_csv("data/attrition_dashboard_data.csv")  

@st.cache_resource
def load_model():
    return joblib.load("model/model.pkl")

df = load_data()
model = load_model()

numeric_features = [
    'Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike',
    'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany',
    'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

ordinal_cols = [
    'Education', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel',
    'JobSatisfaction', 'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'WorkLifeBalance'
]

nominal_cols = ['BusinessTravel', 'Department', 'EducationField', 'Gender',
                'JobRole', 'MaritalStatus', 'OverTime']

ordinal_label_map = {
    "WorkLifeBalance": {
        1: "1 - Low", 2: "2 - Good", 3: "3 - Excellent", 4: "4 - Outstanding"
    },
    "PerformanceRating": {
        1: "1 - Low", 2: "2 - Good", 3: "3 - Excellent", 4: "4 - Outstanding"
    },
    "RelationshipSatisfaction": {
        1: "1 - Low", 2: "2 - Medium", 3: "3 - High", 4: "4 - Very High"
    },
    "JobSatisfaction": {
        1: "1 - Low", 2: "2 - Medium", 3: "3 - High", 4: "4 - Very High"
    },
    "Education": {
        1: "1 - Below College", 2: "2 - College", 3: "3 - Bachelor", 4: "4 - Master", 5: "5 - Doctor"
    },
    "EnvironmentSatisfaction": {
        1: "1 - Low", 2: "2 - Medium", 3: "3 - High", 4: "4 - Very High"
    },
    "JobInvolvement": {
        1: "1 - Low", 2: "2 - Medium", 3: "3 - High", 4: "4 - Very High"
    }
}


# Sidebar Navigation
menu = st.sidebar.radio("Menu", [
    "Data Overview",
    "Feature Importance",
    "Komparasi Fitur terhadap Attrition",
    "Predict Attrition (Inference)",
    "Insights & Recommendations"
])

#  MENU 1: Data Overview
if menu == "Data Overview":
    st.title("📊 Data Overview")
    st.write("Berikut adalah gambaran umum dari dataset yang digunakan:")
    st.dataframe(df)
    st.write("Jumlah data:", df.shape[0])
    st.write("Jumlah fitur:", df.shape[1])
    st.write("Kolom-kolom dalam dataset:", df.columns.tolist())

    # Visualisasi distribusi target
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Attrition', data=df, ax=ax)
    ax.set_title('Distribusi Target: Attrition')
    st.pyplot(fig)

#  MENU 2: Feature Importance 
if menu == "Feature Importance":
    st.title("🔍 Feature Importance dari Model")
    st.write("Berikut adalah fitur-fitur yang paling berpengaruh terhadap prediksi Attrition:")
    if hasattr(model.named_steps['classifier'], 'feature_importances_'):
        feat_names = model.named_steps['preprocessing'].get_feature_names_out()
        importances = model.named_steps['classifier'].feature_importances_
        imp_df = pd.DataFrame({'Feature': feat_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)
        st.dataframe(imp_df)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=imp_df.head(15), x='Importance', y='Feature', ax=ax)
        ax.set_title('Top 15 Important Features')
        st.pyplot(fig)
    else:
        st.warning("Model tidak mendukung feature importance langsung.")

#  MENU 3: Compare Features with Attrition 
elif menu == "Komparasi Fitur terhadap Attrition":
    st.title("📊 Komparasi Fitur terhadap Attrition")
    selected_feature = st.selectbox("Pilih fitur untuk dibandingkan dengan Attrition:", df.columns.drop('Attrition'))
    fig, ax = plt.subplots(figsize=(5, 2))
    if selected_feature in nominal_cols:
        sns.countplot(x=selected_feature, hue='Attrition', data=df, ax=ax)
        ax.set_title(f"{selected_feature} (Nominal) vs Attrition")

    elif selected_feature in ordinal_cols:
        # Mapping ke label deskriptif jika tersedia
        df_viz = df.copy()
        if selected_feature in ordinal_label_map:
            df_viz[selected_feature] = df_viz[selected_feature].map(ordinal_label_map[selected_feature])

        sns.countplot(x=selected_feature, hue='Attrition', data=df_viz, ax=ax)
        ax.set_title(f"{selected_feature} (Ordinal) vs Attrition")

    elif selected_feature in numeric_features:
        sns.boxplot(x='Attrition', y=selected_feature, data=df, ax=ax)
        ax.set_title(f"{selected_feature} (Numerik) vs Attrition")

    else:
        st.warning("Tipe fitur tidak dikenali untuk visualisasi.")
    st.pyplot(fig)

#  MENU 4: Inference / Predict Attrition 
elif menu == "Predict Attrition (Inference)":
    st.title("🤖 Prediksi Attrition dari Input Data")
    st.markdown("Silakan masukkan data karyawan berikut:")

    user_input = {}
    for col in df.columns.drop('Attrition'):
        if df[col].dtype == 'object':
            user_input[col] = st.selectbox(col, options=sorted(df[col].dropna().unique()))
        elif col in ordinal_cols:
            min_val = int(df[col].min())
            max_val = int(df[col].max())
            user_input[col] = st.selectbox(col, options=list(range(min_val, max_val + 1)))
        else:
            user_input[col] = st.number_input(col, value=float(df[col].mean()))



    if st.button("Prediksi"):
        # Convert ke DataFrame dan sesuaikan urutan kolom dengan data latih
        input_df = pd.DataFrame([user_input])
        input_df = input_df[df.drop('Attrition', axis=1).columns]  # Reorder to match training

        # Lakukan prediksi via pipeline
        try:
            prediction = model.predict(input_df)[0]
            result = "⚠️ Karyawan berisiko resign." if prediction == 1 else "✅ Karyawan diprediksi tidak resign."
            st.success(result)
        except Exception as e:
            st.error(f"Terjadi error saat prediksi: {e}")

# === MENU 5: Insight & Recommendations ===
elif menu == "Insights & Recommendations":
    st.title("💡 Insight dan Rekomendasi")
    st.markdown("""
    **Berdasarkan hasil analisis dan modeling, berikut adalah rekomendasi utama untuk HR:**

    1. **Kurangi lembur** — Karyawan dengan status lembur memiliki risiko attrition lebih tinggi.
    2. **Perhatikan penghasilan dasar** — Pendapatan yang rendah cenderung dikaitkan dengan tingkat resign yang tinggi.
    3. **Tingkatkan Work-Life Balance** —  Meskipun bukan fitur terpenting di model, EDA menunjukkan bahwa karyawan dengan WorkLifeBalance rendah lebih sering resign. Program keseimbangan kerja-hidup tetap krusial untuk retensi jangka panjang.
    4. **Fokus pada karyawan dengan masa kerja < 3 tahun** — Kelompok ini menunjukkan tingkat attrition tertinggi.
    5. **Perbanyak pelatihan dan peningkatan karir** — Karyawan yang sering mengikuti pelatihan lebih cenderung bertahan.

    _Dashboard ini bertujuan membantu pengambilan keputusan HR yang lebih tepat berbasis data._
    """)
