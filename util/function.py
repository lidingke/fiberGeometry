

def hex2str(data):
    return " ".join("{:02x}".format(ord(c)) for c in data)