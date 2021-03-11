# Visualisasi - Part 1: Matplotlib

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use("seaborn")

tabel = (pd.read_csv("https://storage.googleapis.com/dqlab-dataset/usia_karyawan.csv")
         .sort_values("Kelompok Usia", ascending=False)
         .set_index("Kelompok Usia")
         )
tabel["Laki-laki"] = -tabel["Laki-laki"]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Perbandingan Jumlah Karyawan Laki-laki dan Perempuan\nBerdasarkan Kelompok Usia",
             x=0., y=1.1, fontsize=24, fontweight='bold', ha="left")
tabel["Laki-laki"].plot(kind="barh", ax=axes[0],
                        color="tab:blue", xlim=[-550, 0])
tabel["Perempuan"].plot(kind="barh", ax=axes[1],
                        color="tab:orange", fontsize=14, xlim=[0, 550])
axes[0].set_ylabel("")
axes[0].set_xticklabels([""])
axes[0].set_yticklabels("")
axes[0].legend(["Laki-laki"], fontsize=14, bbox_to_anchor=(0., 0., 1., .05))
axes[0].set_frame_on(False)
axes[1].set_ylabel("")
axes[1].set_xticklabels([""])
axes[1].legend(["Perempuan"], fontsize=14, bbox_to_anchor=(0., 0., 0.3, .05))
axes[1].set_frame_on(False)
for i, m, w in zip(range(tabel.shape[0]), list(tabel['Laki-laki']), list(tabel['Perempuan'])):
    axes[0].annotate(str(abs(m)), (m+20, i), xytext=(m+20, i),
                     color="w", va="center", ha="center", fontsize=14)
    axes[1].annotate(str(abs(w)), (w-20, i), xytext=(w-20, i),
                     color="w", va="center", ha="center", fontsize=14)
plt.tight_layout()
plt.show()

# Solusi Visualisasi Data 1
# Grafik kolom kurang cocok untuk menampilkan banyak kategori, dalam hal ini adalah rentang usia karyawan.
# Ada tujuh kelompok usia dalam tabel data, masing-masing memiliki keterangan sebanyak 11 karakter (huruf).
# Jika keterangan ini dijejer pada sumbu X, akan melebar dan makan tempat, bukan?

# Pilihan yang lebih baik adalah menggunakan dua bar chart yang disusun menjadi piramida.
# Jenis grafik ini dapat menempatkan batang-batang grafik menjadi lebih berdekatan,
# sehingga menghemat ruang tampilan.
# Dengan ukuran gambar yang sama seperti grafik sebelumnya,
# dimungkinkan juga untuk memilih ukuran huruf lebih besar dan lebih terbaca.

# Sebagai catatan, ada trik khusus jika ingin membuatnya di Excel.
# Pada contoh ini, grafik tersebut sebetulnya terdiri dari dua grafik terpisah,
# masing-masing untuk laki-laki dan perempuan.
# Khusus untuk grafik laki-laki,
# hanya perlu mengubah nilai pada sumbu X menjadi terbaca dari kanan ke kiri (reverse order).
# Selain itu dapat juga mengubahnya pada jendela Format Data Series dalam Excel.
