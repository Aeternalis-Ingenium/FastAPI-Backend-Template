def format_dict_key_to_camel_case(dict_key: str) -> str:
    return "".join(word if idx == 0 else word.capitalize() for idx, word in enumerate(dict_key.split("_")))
