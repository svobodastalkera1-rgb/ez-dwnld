def clear_filename(name):
    forbidden_chars = '<>:"/\\|?*'

    for char in forbidden_chars:
        name = name.replace(char, "_")

    return name.strip()