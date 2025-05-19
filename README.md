# 🎓 Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahaan Jaya Jaya Maju

## 💼 Business Understanding

Perusahaan edutech menghadapi tantangan besar dalam mempertahankan karyawan, khususnya di bidang teknis dan operasional. Tingginya angka *attrition* menyebabkan terganggunya kontinuitas proyek dan peningkatan biaya rekrutmen. Proyek ini bertujuan untuk membantu tim HR memahami pola attrition, melakukan prediksi resign, serta membangun sistem pendukung keputusan berbasis data.

---

## ❓ Permasalahan Bisnis

1. Apa saja faktor utama yang memengaruhi keputusan karyawan untuk keluar dari perusahaan?
2. Dapatkah kita memprediksi kemungkinan seorang karyawan resign?
3. Bagaimana visualisasi data dapat membantu HR memahami dinamika attrition secara menyeluruh?

---

## 📌 Cakupan Proyek

- Pembersihan dan persiapan dataset HR
- Eksplorasi visual terhadap faktor-faktor attrition
- Penanganan data imbalance menggunakan upsampling
- Pelatihan model klasifikasi (Random Forest) menggunakan pipeline
- Penyimpanan model dan pembuatan dashboard interaktif berbasis Streamlit
- Penyusunan insight dan rekomendasi untuk HR

---

## 🧹 Persiapan

**Sumber data**:  
Dataset Dicoding :
🔗 https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

**Setup environment**:
- Python 3.12.6
- Library: `pandas`, `seaborn`, `matplotlib`, `scikit-learn`, `streamlit`, `joblib`
- Visualisasi: Streamlit Dashboard
- Notebook: `notebook.ipynb` (data cleaning, EDA, modeling)

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

## 🛠️ Cara Menjalankan Aplikasi Streamlit Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan aplikasi dashboard ini di komputer lokal Anda:

1. **Clone repository project dari GitHub:**

    ```bash
    git clone https://github.com/AdhiKrisna/Applied-DS-Submission1.git
    cd Applied-DS-Submission1
    ```

2. **Install semua dependencies dari `requirements.txt`:**

    Disarankan menggunakan virtual environment.

    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi Streamlit:**

    ```bash
    streamlit run app.py
    ```

4. **Akses aplikasi di browser:**

    Setelah berhasil dijalankan, buka browser dan akses:

    ```
    http://localhost:8501
    ```

---


