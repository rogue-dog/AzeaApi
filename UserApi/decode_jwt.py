import jwt

def decode(token):
    try:
    
        payload = jwt.decode(token,"Random123",['HS256'])
    except:
        return ("Error",False)
    return (payload['userid'], True)