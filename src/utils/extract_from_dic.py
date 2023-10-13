import json


def extract_name_from_dict(input_dict):
    try:
        if "metadatas" in input_dict and input_dict["metadatas"] and input_dict["metadatas"][0]:
            name_value = input_dict["metadatas"][0][0]["name"]
            result_dict = {"name": name_value}
            return json.dumps(result_dict, indent=2)
    except KeyError:
        return None 