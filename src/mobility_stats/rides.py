import csv
import os
from collections import defaultdict


def load_rides(path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    ride_data = []
    if os.path.exists(path) == False:
        raise FileNotFoundError(f"Could not find file: {path}")

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for reader_dict in reader:
            ride_data.append(
                {
                    "ride_id": reader_dict["ride_id"],
                    "start_station": reader_dict["start_station"],
                    "end_station": reader_dict["end_station"],
                    "duration_min": float(reader_dict["duration_min"]),
                    "rider_type": reader_dict["rider_type"],
                }
            )

    return ride_data


def average_duration(data: list[dict[str, float | int]]) -> float:
    """Return the average ride duration in minutes."""
    if len(data) == 0:
        return 0.0

    sum = 0.0

    for data_dict in data:
        sum += data_dict["duration_min"]

    return sum / len(data)


def count_by_rider_type(data: list[dict[str, float | int]]):
    """Count rides for each rider type."""
    default_dict = defaultdict(int)

    for data_dict in data:
        default_dict[data_dict["rider_type"]] += 1

    return dict(default_dict)


def busiest_start_station(data: list[dict[str, float | int]]):
    """Return the start station with the most rides."""
    if data == None:
        raise ValueError("rides must not be None")

    if len(data) == 0:
        raise ValueError("rides must not be empty")

    stations = {}

    for data_dict in data:
        rides = data_dict["start_station"]
        stations[rides] = stations.get(rides, 0) + 1

    return max(stations, key=stations.get)


def filter_long_rides(data: list[dict[str, float | int]], threshold: int = 30):
    """Return all rides with duration greater than or equal to b minutes."""
    long_rides = []

    for data_dict in data:
        if data_dict["duration_min"] >= threshold:
            long_rides.append(data_dict)

    return long_rides
