from roboflow import Roboflow
from skimage import img_as_ubyte
from skimage import io
from skimage.draw import rectangle_perimeter
import pandas as pd
import numpy as np
import json

import cv2

from detect_vehicle import count_vehicle

# Memasukkan path gambar yang ingin dideteksi
image_paths = ['imgs/SoettaBubatTimur.png', 'imgs/SoettaBubatBarat.png', 'imgs/SoettaBubatSelatan.png', 'imgs/SoettaBubatUtara.png']

# Memanggil fungsi deteksi kendaraan dari detect_vehicle.py
total, detail, bobot = [], [], []  # Dataframe untuk menyimpan hasil deteksi dari setiap gambar

for path in image_paths:
    count_sum, pred, weight = count_vehicle(path)
    total.append(count_sum)
    detail.append(pred)
    bobot.append(weight)

intersection_road = ['Arah Timur - Samsat', 'Arah Barat - Batununggal', 'Arah Selatan - Exit Tol', 'Arah Utara - BKR']

baseTimer = 300  # baseTimer = int(input("Enter the base timer value"))
timeLimits = [20, 110]  # timeLimits = list(map(int,input("Enter the time limits ").split()))

# print("Input no of vehicles : ", *no_of_vehicles)
print(f"\n\n\nTotal kendaraan di persimpangan Soekarno-Hatta & Buah Batu: {sum(total)} Kendaraan")
print(f'Durasi maksimal 4 persimpangan: {baseTimer} detik')
print(f'Durasi minimal dan maksimal per persimpangan: minimal {timeLimits[0]} detik, maksimal {timeLimits[1]} detik\n')

t = [(i / sum(bobot)) * baseTimer if timeLimits[0] < (i / sum(bobot)) * baseTimer < timeLimits[1] 
else min(timeLimits, key=lambda x: abs(x - (i / sum(bobot)) * baseTimer)) for i in bobot]

for name, idx, det, time in zip(intersection_road, total, detail, t):
    print(f'Jumlah Kendaraan terhitung dari {name} : {idx} kendaraan.')

    for key, value in det.items():
        print(f"{key}: {value}") 

    print(f'Kalkulasi durasi lampu hijau adaptif: {int(time)} detik\n\n')


