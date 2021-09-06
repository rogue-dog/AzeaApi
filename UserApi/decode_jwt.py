import jwt

def decode(token):
    payload = jwt.decode(token,"Random123",['HS256'])
    return payload['userid']