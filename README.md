# AI-Driven-Intersections-Traffic-Light
AI traffic management at the Soekarno-Hatta and Buah Batu intersection through CCTV ATCS Dishub Bandung


### Try in local device or github codespaces
```
git clone https://github.com/rafka-imandaputra/AI-Driven-Intersections-Traffic-Light.git .

python -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install roboflow numpy pandas scikit-image opencv-python

python main.py
```


### Sample output
```
Total kendaraan di persimpangan Soekarno-Hatta & Buah Batu: 162 Kendaraan
Durasi maksimal 4 persimpangan: 300 detik
Durasi minimal dan maksimal per persimpangan: minimal 20 detik, maksimal 110 detik

Jumlah Kendaraan terhitung dari Arah Timur - Samsat : 33 kendaraan.
cars: 20
motorcycle: 13
Kalkulasi durasi lampu hijau adaptif: 60 detik


Jumlah Kendaraan terhitung dari Arah Barat - Batununggal : 58 kendaraan.
cars: 29
motorcycle: 25
truck: 3
bunch of motorcycle: 1
Kalkulasi durasi lampu hijau adaptif: 102 detik


Jumlah Kendaraan terhitung dari Arah Selatan - Exit Tol : 36 kendaraan.
cars: 25
motorcycle: 9
truck: 2
Kalkulasi durasi lampu hijau adaptif: 78 detik


Jumlah Kendaraan terhitung dari Arah Utara - BKR : 35 kendaraan.
cars: 19
motorcycle: 16
Kalkulasi durasi lampu hijau adaptif: 59 detik
```
