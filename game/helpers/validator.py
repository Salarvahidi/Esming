from rest_framework import serializers


def check_values(data):
    field_values = {}
    for item in data:
        for key, value in item["values"].items():
            if not field_values.get(key):
                field_values[key] = {}
            try:
                field_values[key][value] += 1
            except KeyError:
                field_values[key][value] = 0
    return field_values


def score(letter, check_value, data):
    return [
        {
            "user": item["user"],
            "values": {
                key: (
                    (value, 0)
                    if not value.startswith(letter)
                    else (value, 5 if check_value[key][value] >= 1 else 10)
                )
                for key, value in item["values"].items()
            },
        }
        for item in data
    ]
