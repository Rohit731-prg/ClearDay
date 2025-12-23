from passlib.hash import sha256_crypt as bcript

def generatehash(password: str) -> str:
    return bcript.hash(password)

def compairPassword(password: str, hash: str) -> bool:
    return bcript.verify(password, hash)