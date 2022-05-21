# Write a small function to remove certain keys from a nested dict.

# For example:
my_dict = {
    "name": "smith",
    "contact_details": {
        "address": "abcd",
        "phone": "1234",
        "suburb": "sydney",
        "name": "customer_name",
    },
    "score": 3,
    "tasks": ["task one", "task two"],
}
key_list = ["name", "phone"]


def remove_keys(my_dict: dict, key_list: list = None) -> dict:
    # do the job, remove keys which matches in `key_list`
    [my_dict.pop(k) for k in key_list if k in my_dict]
    # Loop through dictionary and recursively call the function
    for k, v in my_dict.items():
        if isinstance(v, dict):
            remove_keys(v, key_list)
        else:
            continue
    return my_dict


assert remove_keys(my_dict, key_list) == {
    "contact_details": {"address": "abcd", "suburb": "sydney"},
    "score": 3,
    "tasks": ["task one", "task two"],
}
