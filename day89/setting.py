import hashlib,time

class DebugConfig(object):
    DEBUG = True
    SECRET_KEY = "#$%^&*($#$%^&*%$#$%^&*^%$#$%"
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_NAME = "I am Not Session"


class TestConfig(object):
    TESTING = True
    SECRET_KEY = hashlib.md5(f"{time.time()}#$%^&*($#$%^&*%$#$%^&*^%$#$%{time.time()}".encode("utf8")).hexdigest()
    PERMANENT_SESSION_LIFETIME = 360000
    SESSION_COOKIE_NAME = "#$%^&*($#$%^&*%$#$%^&*^%$#$%"