def full_name(first_name, last_name, capitalize=False):
    if capitalize:
        return f"{first_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name} {last_name}"
    
print(full_name("lenon", "john", capitalize=True))