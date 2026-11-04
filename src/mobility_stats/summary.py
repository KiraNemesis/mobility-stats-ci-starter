from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(rides):
    """Build a compact dictionary with headline statistics."""
    dict_ = {
        "ride_count": len(rides),
        "average_duration": average_duration(rides),
        "rider_types": count_by_rider_type(rides),
    }
    if rides:
        dict_["busiest_start_station"] = busiest_start_station(rides)
    else:
        dict_["busiest_start_station"] = None

    return dict_


def format_summary(rides):
    """Create a human-readable text summary."""
    title = "Mobility summary"
    line1 = f"Rides: {rides['ride_count']}"
    line2 = f"Average duration: {rides['average_duration']:.1f} min"
    line3 = f"Busiest start: {rides['busiest_start_station']}"

    return title + "\n" + line1 + "\n" + line2 + "\n" + line3
