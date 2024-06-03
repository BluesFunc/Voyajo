

def hash_password(password: str):
    return password + "hash_string"


def check_password_equality(origin_password:str, password: str):
    return origin_password == hash_password(password)