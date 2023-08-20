from roboflow import Roboflow

import pandas as pd
import numpy as np


def weighting(count) :
    counts = count.to_frame().T.reset_index(drop = True)
    motorcycle = 1
    car = 4
    truck = 6
    bus = 6
    motor_bunch = 0
    ambulance = 30
    
    data = pd.DataFrame(
        columns = ['motorcycle', 'cars', 'truck', 'bus', 'bunch of motorcycle', 'ambulance']
    )
    # print(data)
    # print(counts)
    data = pd.concat([data, counts], axis = 0).fillna(0)
    # print(data.columns)
    data = data * np.array([[motorcycle, car, truck, bus, motor_bunch, ambulance]])
    return data.sum(axis = 1)[0]


def count_vehicle(img_path, confidence=4, overlap=60):
    rf = Roboflow(api_key="wQcOF2Ddx27YrNWByG2M")
    project = rf.workspace().project("bandung-buah-batu-cctv-traffic")
    model = project.version(5).model

    inference = model.predict(img_path, confidence=confidence, overlap=overlap).json()

    predictions = inference['predictions']
    df = pd.DataFrame(predictions)

    total = df.shape[0]
    pred = df['class'].value_counts()
    weight = weighting(pred)

    return total, pred.to_dict(), weight

