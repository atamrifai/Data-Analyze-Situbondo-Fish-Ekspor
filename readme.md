# Laporan Proyek Machine Learning - Atam RIfa'i Sujiwanto

## Domain Proyek

Setiap wilayah di Indonesia memiliki banyak sekali sumber daya alam termasuk produksi ikan,salah satunya adalah ikan laut. Dari sumber daya alam tersebut banyak para nelayan menjadikan hal tersebut sebagai salah satu pekerjaan mereka yaitu menangkap ikan. [1] Perdagangan dalam sektor perikanan yang mengalami ekspor tanpa mengetahui batasan dari nilai yang di ekspor terhadap barang yang di ekspor akan mengalami masalah dalam jumlah nilai. Seperti penelitian sebelumnya [2] pada daerah ternate. Namun, pada kasus ini ingin mengangkat topik tentang  _clustering_ hasil ekspor ikan di kabupaten saya Situbondo, dengan mengekspor jumlah ikan keluar kabupaten Situbondo tanpa adanya pengelompokan dari jumlah yang di ekspor, dengan metode _clustering_ sehingga menjadi _clustering_ Melimpah, _clustering_ Cukup, _clustering_ kurang pada proyek kali ini saya akan membuat _clustering_ berdasarkan jenis ikan yang di ekspor pada tahun 2017.
 
## _Business Understanding_

Dengan adanya pengklasifikasian pada jenis hasil laut yang di ekspor keluar Kabupaten Situbondo, maka beberapa hal yang dapat terbantu mulai dari pengelompokkan terhadap jenis ikan, volume ikan, dan harga ikan.

### _Problem Statements_

Menjelaskan pernyataan masalah latar belakang:
- Belum mengetahui hasil jenis ikan terbanyak pada tahun 2017 berdasarkan kelompok melimpah
- Belum mengetahui hasil jenis ikan terbanyak pada tahun 2017 berdasarkan kelompok kurang
- Supaya dapat menyeimbangkan hasil ditahun berikutnya untuk meningkatkan pendapatan daerah

### _Goals_

Menjelaskan tujuan dari pernyataan masalah:
- Untuk mengetahui hasil ekspor jenis ikan yang masuk _cluster_ melimpah pada tahun 2017
- Untuk mengetahui hasil ekspor jenis ikan yang masuk _cluster_ kurang pada tahun 2017
- Untuk menyeimbangkan hasil ekspor pada tahun-tahun berikutnya untuk meningkatkan pendapatan daerah


### _Solution Statements_
- Untuk menyelesaikan permasalahan tersebut penulis menggunakan Algoritma Clustering yang dibantu dengan Algoritma Euclidean Distance menggunakan _native_ di python
- Mendapatkan hasil dari _clustering_ sehingga dapat mengelompokkan jenis jenis ikan
- Evaluasi Metrik yang digunakan adalah dengan memberi batasan antara _cluster_ melimpah, _cluster_ cukup, dan _cluster_ kurang. Berdasarkan _tuning_ dari pengklasifikasian 3 kelompok

## _Data Understanding_
Dataset yang digunakan dalam kasus ini berasalah dari sumber terpercaya skala nasional, yaitu BPPS Indonesia[3].

### Variabel-variabel pada Data Ekspor Ikan 2017 Situbondo dataset adalah sebagai berikut:
- Jenis Ikan : Merupakan ragam jenis ikan yang berhasil di ekspor pada tahun 2017.
- TON : Merupakan total dari bobot yang di ekspor berdasarkan jenis ikan pada tahun 2017
- RP (OOO) : Merupakan harga jual yang di dapat dari hasil ekspor pada tahun 2017

### Pengelolaan Clustering
Pada data akan ditampilkan clustering berdasarkan banyaknya ikan yang di ekspor dan hasil penjualan ikan tersebut. dari 2 variable itulah (TON, RP (000)) akan didapatkan clustering pada tahun 2017

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Tahap 1 : Memasukkan _Library_ yang digunakan berasal dari, OS untuk mengelola directory pada file, Copy digunakan saat membuat _Algoritma Euclidien_ , Numpy digunakan untuk mengelola data menjadi _list, array_ , Pandas digunakan untuk mengelola file data menjadi objek dalam python, Matplotlib digunakan untuk membuat visualisasi data
```
import os
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
```

- Tahap 2 : Import data menggunakan pandas dengan membaca data dari excel. sehingga akan menampilkan data seperti ini :

![image](https://user-images.githubusercontent.com/58683035/183570605-e94b0c1b-c794-4a7b-8288-0c1280613119.png)


- Tahap 3 : Menampilkan informasi data dengan menggunakan df.info() untuk melihat jenis data, ketersediaan data setiap kolom, dan jenis jenis colom. kemudian menggunakan df.describe() untuk mengetahui persebaran data. sehingga tampilannya :

![image](https://user-images.githubusercontent.com/58683035/183570683-0e6e9c83-eef4-4ac8-ad3a-e8370c2124d1.png)


- Tahap 4 : Plotting data terhadap kanvas menggunakan fungsi plt.scatter. secara general. ini berfungsi untuk mengetahui proses persebaran data terhadap variable TON dan RP

![image](https://user-images.githubusercontent.com/58683035/183570785-6c2437e1-8149-4cde-9c11-6cd4c6017974.png)


- Tahap 5 : Merumuskan algoritma _Euclidean Distance_
```
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)
```
- Tahap 6 : Menjalankan Algoritma untuk menciptakan _clustering_ sehingga didapat sebagai berikut

![image](https://user-images.githubusercontent.com/58683035/183570879-38a2502f-d3e0-4c87-b240-750f2616781d.png)

- Tahap 7 : Setelah menjankan clustering maka hasilnya akan nampak seperti tabel berikut ini: 


![image](https://user-images.githubusercontent.com/58683035/183570962-ecbcbef1-c56c-42f7-8027-9da47795b114.png)


## Modeling
Pada algoritma ini mneggunakan algoritma Euclidean Distance dengan membagi kelompok cluster menjadi 3 bagian yaitu 0, 1, 2 artinya 0=Terbanyak, 1=Cukup, 2=kurang. dan dibandingkan dengan algoritma dari K-Means Scikit Learn mendapatkan hasil performa yang sama.

### Hasil Clustering Menggunakan Algoritma ScikitLearn

![image](https://user-images.githubusercontent.com/58683035/183571122-f75b947d-12c9-4c53-8d67-8b91ef44ad27.png)

### Hasil Clustering Menggunakan Algoritma Mandiri (Euclidien Distance)

![image](https://user-images.githubusercontent.com/58683035/183571240-3e5a2394-33b7-4ceb-bc89-ee70978700a8.png)


## Evaluation

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik menggunakan algoritma Euclidean distance yang menempatkan titik terdekat dengan titik terbanyak. Jelaskan mengenai beberapa hal berikut:
- Metrik yang digunakan menunjukkan bahwa terdapat 2 titik di hasil melimpah, 4 titik di hasil sedang dan sisanya masih kurang dengan tabel sebagai berikut :
```
       Jenis Ikan Cluster
0          Layang     0.0
1         Kembung     1.0
2          Kerapu     2.0
3         Tongkol     0.0
4         Tengiri     1.0
5       Bambangan     2.0
6           Selar     1.0
7            Teri     1.0
8          Lemuru     1.0
9           Layur     1.0
10          Petek     1.0
11          Cucut     1.0
12        Manyung     1.0
13        P a r i     1.0
14         Beloso     1.0
15  Udang Lainnya     2.0
16          Kakap     2.0
17         Kurisi     1.0
18        Lainnya     1.0
19      Cumi-Cumi     1.0
20    Bawal putih     1.0
21        Belanak     1.0
22       Rajungan     1.0
23       Beronang     1.0
24       Kepiting     1.0
```

## References
[1] Muhammad Y Rizki, Fira Fania, Agus P Windarto, 2017 "IMPLEMENTASI K-MEANS CLUSTERING DALAM MENGELOMPOKKAN JUMLAH PENJUALAN IKAN LAUT DI TPI MENURUT WILAYAH". JIKO (Jurnal Informatika dan Komputer) Vol. 3, No. 2, Agustus 2020, hlm. 69-74

[2] R. J. Hablum., A. Khairan dan R. Rosihan., 2019., “Clustering Hasil Tangkap Ikan Di Pelabuhan Perikanan Nusantara (PPN) Ternate Menggunakan Algoritma K-Means,” JIKO (Jurnal Informatika dan Komputer)., vol. 2, no. 1, pp. 26-33

[3] BPPS Statistik. diakses pada 08/08/2022. https://situbondokab.bps.go.id/statictable/2017/06/02/485/produksi-dan-nilai-perikanan-tangkap-menurut-jenis-ikan-di-kabupaten-situbondo-2015---2016.html


**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

