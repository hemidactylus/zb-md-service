import base64


def encode(sng):
    return base64.b64encode(sng.encode()).decode()


def decode(b64):
    return base64.b64decode(b64).decode()
