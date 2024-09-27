# Example 1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Example 2

import pandas as pd
import numpy as np

# load weather data
weather_df = pd.DataFrame('april2024_station_data.csv')

# Numpy is faster so convert
wind_speed = df['wind_speed'].to_numpy()
wind_direction = df['wind_direction'].to_numpy()

# Better built in function in np
wind_direction_rad = np.deg2rad(wind_direction)