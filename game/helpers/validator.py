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
    scores = []
    zero = []
    for value in data:
        user = value["user"]
        new_data = {}
        new_data["user"] = user
        new_data["values"] = {}
        for key, val in value["values"].items():
            if not val.startswith(letter) or not val:
                new_data["values"][key] = [val, 0]
                zero.append({user: key})
            elif check_value[key][val] >= 1:
                new_data["values"][key] = [val, 5]
            else:
                new_data["values"][key] = [val, 10]
        scores.append(new_data)
    return scores, zero
