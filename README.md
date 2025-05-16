# Employee Data

## 🧾 Feature Explanation (Grouped by Data Type)

The dataset contains demographic details, work-related metrics, and attrition flag. Features are grouped into **numerical**, **ordinal**, and **nominal** for better preprocessing and modeling clarity.

---

### 🔢 Numerical Features (Continuous or Countable)

These are continuous or countable variables, ideal for mathematical operations and scaling:

- **Age** – Age of the employee  
- **DailyRate** – Daily salary  
- **DistanceFromHome** – Distance from work to home (in km)  
- **HourlyRate** – Hourly salary  
- **MonthlyIncome** – Monthly salary  
- **MonthlyRate** – Monthly rate  
- **NumCompaniesWorked** – Number of companies worked at  
- **PercentSalaryHike** – The percentage increase in salary last year  
- **TotalWorkingYears** – Total years worked  
- **TrainingTimesLastYear** – Number of trainings attended last year  
- **YearsAtCompany** – Years at company  
- **YearsInCurrentRole** – Years in the current role  
- **YearsSinceLastPromotion** – Years since the last promotion  
- **YearsWithCurrManager** – Years with the current manager  

---

### 📊 Ordinal Features (Ranked Categories)

These are categorical features that have meaningful order or hierarchy. They are encoded using **OrdinalEncoder**:

- **Education** – (1 = Below College, 2 = College, 3 = Bachelor, 4 = Master, 5 = Doctor)  
- **EnvironmentSatisfaction** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **JobInvolvement** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **JobLevel** – Job level from 1 (lowest) to 5 (highest)  
- **JobSatisfaction** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **PerformanceRating** – (1 = Low, 2 = Good, 3 = Excellent, 4 = Outstanding)  
- **RelationshipSatisfaction** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **StockOptionLevel** – Level of stock option awarded (0–3)  
- **WorkLifeBalance** – (1 = Low, 2 = Good, 3 = Excellent, 4 = Outstanding)  

---

### 🧩 Nominal Features (Unordered Categories)

These are categorical features with no inherent order. They are encoded using **One-Hot Encoding**:

- **BusinessTravel** – Travel frequency (e.g., Rarely, Frequently)  
- **Department** – Department of the employee  
- **EducationField** – Employee’s field of education  
- **Gender** – Male / Female  
- **JobRole** – Employee’s job role  
- **MaritalStatus** – Marital status (Single, Married, Divorced)  
- **OverTime** – Whether the employee works overtime (Yes / No)  

---

### 🗑️ Droppable Columns

These features do not contribute to the analysis or are constant:

- **EmployeeId** - Identifier only  
- **EmployeeCount** - Constant value  
- **Over18** - Constant (all employees over 18)  
- **StandardHours** - Constant (value = 80 for all)  


## Acknowledgements
https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-for-hr-retaining-valuable-employees/

# Employee Attrition Analysis Project

## 📌 Business Understanding

Departemen HR menghadapi masalah tingginya *employee attrition* yang berdampak langsung pada stabilitas perusahaan. Proyek ini bertujuan untuk mengidentifikasi faktor utama penyebab attrition dan menyediakan insight untuk strategi retensi karyawan yang lebih baik.

---

## 🧠 Data Understanding

Dataset berisi informasi demografis dan pekerjaan dari karyawan. Target yang dianalisis adalah kolom `Attrition` (0 = Tidak, 1 = Ya).

Referensi dataset: [IBM HR Analytics](https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-for-hr-retaining-valuable-employees/)

---

## 🧹 Data Preparation

- Drop kolom tidak relevan: `EmployeeId`, `Over18`, `StandardHours`
- Encode kolom kategorikal dengan `LabelEncoder`
- Standardisasi fitur numerik menggunakan `StandardScaler`
- Split dataset menjadi training dan testing (80:20)

---

## 📊 Exploratory Data Analysis (EDA)

Visualisasi dilakukan untuk menggali insight awal terhadap data:

- **Distribusi attrition**: mayoritas karyawan tetap
- **OverTime vs Attrition**: karyawan lembur cenderung lebih banyak keluar
- **MonthlyIncome**: income rendah cenderung lebih banyak resign
- **JobSatisfaction & EnvironmentSatisfaction**: tingkat kepuasan rendah berkorelasi dengan attrition
- **YearsAtCompany**: attrition tinggi pada masa kerja < 3 tahun

---

## 📈 Modeling

- Algoritma: `RandomForestClassifier`
- Metode evaluasi: `confusion matrix`, `classification report`
- Hasil: Akurasi di atas 80% dengan recall yang baik untuk prediksi kelas `Attrition = 1`
- Model dan scaler disimpan di folder `model/` dalam format `.pkl`

---

## 💡 Insights & Recommendations

Berdasarkan hasil analisis data dan modeling, berikut adalah rekomendasi utama yang dapat diterapkan oleh departemen HR untuk menurunkan tingkat attrition:

1. **Kurangi lembur**  
   Karyawan dengan status lembur (*OverTime = Yes*) memiliki kecenderungan lebih tinggi untuk resign. Penyesuaian beban kerja atau sistem shift dapat membantu.

2. **Perhatikan penghasilan dasar**  
   Karyawan dengan pendapatan bulanan rendah terlihat lebih rentan keluar dari perusahaan. Strategi kenaikan gaji yang adil perlu dipertimbangkan, terutama untuk level pekerjaan rendah.

3. **Tingkatkan Work-Life Balance**  
   Meskipun bukan fitur terpenting di model, EDA menunjukkan bahwa karyawan dengan WorkLifeBalance rendah lebih sering resign. Program keseimbangan kerja-hidup tetap krusial untuk retensi jangka panjang.

4. **Fokus pada karyawan dengan masa kerja < 3 tahun**  
   Kelompok karyawan baru (0–3 tahun masa kerja) menunjukkan tingkat attrition tertinggi. Perlu program onboarding dan mentoring yang kuat untuk meningkatkan loyalitas awal.

5. **Perbanyak pelatihan dan peluang pengembangan karir**  
   Karyawan yang sering mengikuti pelatihan cenderung bertahan lebih lama. Program pengembangan karir dapat membantu mengurangi turnover dari sisi motivasi intrinsik.

---

## 📦 Cara Menjalankan Aplikasi Streamlit

Untuk melihat dashboard interaktif bisnis, ikuti langkah-langkah berikut:

1. **Install dependencies** terlebih dahulu:

```bash
pip install -r requirements.txt

2. **Jalankan command** untuk run file streamlit
```bash
streamlit run app.py
