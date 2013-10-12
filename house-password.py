def checkio(data):
    if len(data)>9:
        if any(i.isupper() for i in data) and any(i.islower() for i in data) and any(i.isdigit() for i in data):
            return True
        else:
            return False
    else:
        return False