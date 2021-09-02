import jwt


def encode(data):
    token = jwt.encode(data, "Random123", algorithm="HS256")
    return token
