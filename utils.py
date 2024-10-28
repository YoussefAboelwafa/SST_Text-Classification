def map_classes(score):
    if 0 <= score <= 0.2:
        return 0  # Very negative
    elif 0.2 < score <= 0.4:
        return 1  # Negative
    elif 0.4 < score <= 0.6:
        return 2  # Neutral
    elif 0.6 < score <= 0.8:
        return 3  # Positive
    elif 0.8 < score <= 1.0:
        return 4  # Very positive
    else:
        return None  # If score is out of range