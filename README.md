# Kalkulator-Statistika
Kalkulator statistika GUI Kivy python Sederhana untuk melakukan penghitungan Statistika Dasar.

# untuk Mencoba aplikasi
```sh
$ python3 main.py
```

# Cara Build Ke Apk Android
  - install buildozer https://github.com/kivy/buildozer gunakan python3
  - Download python3 crystax https://www.crystax.net/en/download
```sh
$ cd path/project/kamu
$ buildozer init
```
  - akan muncul buildozer.spec buka file itu dan edit beberapa baris berikut
```sh
source.include_exts = py,kv,ttf
requirements = python3crystax==3.6,kivy
android.ndk_path = ~/path/ke/HasilExtarctPython3crystaxYangDiDownloadTadi
log_level = 2
```
  - Lalu Ketik Perintah
```sh
$ buildozer android debug
```
  - File apk akan ada pada folder bin dalam project kalian
  
  Semoga Beruntung :)
