def process_data(data):
    # Simulate data processing (e.g., summing numbers in a list)
    if not isinstance(data, list):
        return "Invalid data format. Expected a list of numbers."
    try:
        result = sum(data)
    except TypeError:
        return "Data contains non-numeric values."
    return f"Processed data: sum is {result}"
