def validate_decimals(value):
    try:
        return round(float(value), 2)
    except Exception as e:
        print(e)
        raise e
