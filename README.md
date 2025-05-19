# 📊 Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahaan Jaya Jaya Maju

## 💼 Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang berdiri sejak tahun 2000 dan telah memiliki lebih dari 1000 karyawan yang tersebar di seluruh Indonesia.  
Namun, perusahaan menghadapi tantangan serius dalam mempertahankan karyawan, dengan attrition rate yang dilaporkan mencapai lebih dari 10%. Hal ini berdampak pada produktivitas, stabilitas tim, serta biaya operasional HR seperti rekrutmen dan pelatihan karyawan baru.

Sebagai bentuk respon terhadap permasalahan ini, tim HR perusahaan ingin:
- Mengidentifikasi faktor-faktor yang memengaruhi keputusan karyawan untuk keluar dari perusahaan
- Memprediksi kemungkinan resign menggunakan pendekatan machine learning
- Menyusun business dashboard yang mendukung monitoring kondisi HR secara interaktif dan informatif

---

## ❓ Permasalahan Bisnis

1. Tingginya **attrition rate (>10%)** yang menyebabkan beban tambahan bagi divisi HR
2. Kurangnya pemahaman mendalam tentang **faktor penyebab utama attrition/resign rate yang tinggi**
3. Belum adanya sistem prediktif dan visualisasi data untuk mendukung pengambilan keputusan oleh manajer HR

---

## 📌 Cakupan Proyek

- Analisis eksploratif untuk memahami pola dan distribusi data karyawan
- Penerapan preprocessing (scaling, encoding, handling missing values)
- Penanganan imbalance data menggunakan teknik upsampling
- Pembangunan model machine learning menggunakan pipeline dan Random Forest
- Pembuatan dashboard interaktif berbasis Streamlit
- Penyusunan insight dan rekomendasi actionable bagi tim HR

---

## 🧹 Persiapan

### ✅ Sumber Data

🔗 Link dataset: [https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Dataset yang digunakan adalah dataset karyawan dari Dicoding yang berisi data demografis dan atribut pekerjaan karyawan. Berikut ini adalah pembagian kategori fitur dataset:

### 🔢 Numerical Features (Continuous or Countable)

Ini adalah variabel kontinu atau terhitung, ideal untuk operasi matematika dan scalling:

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

### 📊 Ordinal Features (Ranked Categories)

Ini adalah fitur kategoris yang memiliki urutan atau hierarki yang berarti. Fitur-fitur ini dikodekan menggunakan **OrdinalEncoder**:

- **Education** – (1 = Below College, 2 = College, 3 = Bachelor, 4 = Master, 5 = Doctor)  
- **EnvironmentSatisfaction** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **JobInvolvement** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **JobLevel** – Job level from 1 (lowest) to 5 (highest)  
- **JobSatisfaction** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **PerformanceRating** – (1 = Low, 2 = Good, 3 = Excellent, 4 = Outstanding)  
- **RelationshipSatisfaction** – (1 = Low, 2 = Medium, 3 = High, 4 = Very High)  
- **StockOptionLevel** – Level of stock option awarded (0–3)  
- **WorkLifeBalance** – (1 = Low, 2 = Good, 3 = Excellent, 4 = Outstanding)  

### 🧩 Nominal Features (Unordered Categories)

Ini adalah fitur kategoris yang memiliki urutan atau hierarki yang berarti. Fitur-fitur ini dikodekan menggunakan  **One-Hot Encoding**:

- **BusinessTravel** – Travel frequency (e.g., Rarely, Frequently)  
- **Department** – Department of the employee  
- **EducationField** – Employee’s field of education  
- **Gender** – Male / Female  
- **JobRole** – Employee’s job role  
- **MaritalStatus** – Marital status (Single, Married, Divorced)  
- **OverTime** – Whether the employee works overtime (Yes / No)  

### 🗑️ Droppable Columns

Fitur-fitur ini tidak berkontribusi pada analisis atau bersifat konstan:

- **EmployeeId** - Identifier only  
- **EmployeeCount** - Constant value  
- **Over18** - Constant (all employees over 18)  
- **StandardHours** - Constant (value = 80 for all)  

### 🖥️ Setup Environment (Menggunakan venv Python)

- Python 3.12.6
- Library: `pandas`, `seaborn`, `matplotlib`, `scikit-learn`, `streamlit`, `joblib`
- Visualisasi: Streamlit Dashboard
- Notebook: `notebook.ipynb` (data cleaning, EDA, modeling)

Ikuti langkah-langkah berikut untuk menyiapkan environment proyek ini:

1. **Buat virtual environment**:

    ```bash
    python -m venv env
    ```

2. **Aktifkan virtual environment**:

    - Windows:
      ```bash
      .\\env\\Scripts\\activate
      ```
    - Mac/Linux:
      ```bash
      source env/bin/activate
      ```

3. **Install semua dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### 🛠️ Cara Menjalankan Aplikasi

1. **Clone repository:**

    ```bash
    git clone https://github.com/AdhiKrisna/Applied-DS-Submission1.git
    cd Applied-DS-Submission1
    ```

2. **Aktifkan virtual environment dan install dependensi**  
   (lihat langkah Setup Environment di atas)

3. **Jalankan aplikasi Streamlit:**

    ```bash
    streamlit run app.py
    ```

4. **Akses aplikasi di browser:**

    ```
    http://localhost:8501
    ```

### 🔍 Cara Menjalankan File Prediksi (Opsional)

Selain menggunakan Streamlit, kamu juga dapat menjalankan prediksi secara langsung menggunakan file Python `prediction.py` yang telah disediakan.

### Langkah-langkah:

1. Pastikan virtual environment sudah aktif (lihat bagian Setup Environment)
2. Jalankan script berikut di terminal:

    ```bash
    python prediction.py
    ```

File ini akan menampilkan hasil prediksi berdasarkan data baru (simulasi) yang telah dimasukkan di dalam script.

Contoh output:
✅ Karyawan diprediksi tidak resign.
⚠️ Karyawan berisiko resign.

---

## 📊 Business Dashboard

Aplikasi Streamlit menyediakan 5 menu utama:
1. **Feature Importance** – Menampilkan ranking fitur berdasarkan pengaruh terhadap prediksi attrition.
2. **Komparasi Fitur vs Attrition** – Memungkinkan user membandingkan setiap fitur terhadap tingkat attrition secara visual (dengan label deskriptif untuk ordinal).
3. **Prediksi Attrition (Inference)** – Input form untuk memprediksi kemungkinan resign berdasarkan data karyawan baru.
4. **Distribusi Data** – Menampilkan distribusi kelas dan hasil balancing dataset.
5. **Insight & Rekomendasi** – Menampilkan hasil analisis dan saran strategi retensi karyawan.

---

## ✅ Conclusion

Model machine learning berhasil dibangun menggunakan Random Forest dengan akurasi di atas 80%.  
Fitur-fitur seperti `Age`, `MonthlyIncome`, `OverTime`, dan `TotalWorkingYears` terbukti memiliki pengaruh besar dalam menentukan apakah seorang karyawan akan keluar dari perusahaan.  
Dashboard interaktif juga memberikan kemudahan eksplorasi dan interpretasi hasil bagi pihak HR.

---

## 🚀 Rekomendasi Action Items

1. **Kurangi lembur berlebihan**  
   Karyawan yang lembur memiliki risiko resign lebih tinggi.

2. **Optimalkan kompensasi dasar**  
   Pendapatan rendah secara signifikan berkorelasi dengan keputusan resign.

3. **Tingkatkan program onboarding untuk karyawan baru (<3 tahun)**  
   Masa kerja singkat memiliki attrition tertinggi – mentoring dan career path penting.

4. **Fasilitasi pelatihan dan pengembangan karir**  
   Karyawan yang terlibat aktif dalam pelatihan cenderung bertahan lebih lama.

5. **Evaluasi kembali kebijakan Work-Life Balance**  
   Meskipun bukan fitur paling penting dalam model, EDA menunjukkan korelasi negatif antara skor WLB dan attrition.

---
