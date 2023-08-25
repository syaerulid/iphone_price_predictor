# Prediksi Harga iPhone
Repo tentang Prediksi Harga Iphone menggunakan Machine Learning Metode Regresi<br>
<br>
Dataset model ini diperoleh dengan cara Webscraping menggunakan Selenium dan BeautifulSoup pada Web Shopee pada 6 Toko yang berbeda
<br>

Tujuan Model: Untuk Memprediksi Harga Apple iPhone berdasarkan Model, Memory dan juga Varian (dimana terdapat 4 Varian)

Data Cleaning : Hapus Inkonsistensi Data, Mengganti nama kolom, menghapus punctuation dari text dalam kolom, membuat kolom baru sebelum permodelan<br><br>
Metode Statistik yang digunakan beberapa adalah sebagai berikut:<br>
Deskriptive Statistics, Pearson dan Spearman Correlation, ANOVA<br>
<br>
Untuk Mengecek Metode Data Cleaning, Statistikal Analisis dan Visualisasi yang lebih lengkap<br>
silahkan cek disini:<br>
https://bit.ly/3EvKgPb

Model ini memiliki R2-Squared Score sebesar 0.96xx, artinya model ini mampu menangkap variansi dari Features sebesar 96%<br>
meskipun terdapat penurunan R2-Squared Score dari training data diangka 0.99 menjadi 0.96 untuk testing data<br>
tapi, penurunan tersebut masih dapat ditoleransi, karena tidak banyak model yang mampu memprediksi secara sempurna

Dibawah ini adalah demo dari Model Prediksi Harga iPhone:

https://github.com/syaerulid/iphone_price_predictor/blob/main/demo/flask_fast.gif

![image](https://github.com/syaerulid/iphone_price_predictor/assets/119069839/2ae1f27d-81e5-43b5-bd94-02188649b5bd)

