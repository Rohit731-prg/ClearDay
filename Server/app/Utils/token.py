from jose import jwt
from app.Config.Config import setting
from datetime import timedelta, timezone

secret_key = setting.SERECT_KEY
algo = "HS256"
expair_min = 300

def generaytToken(data: dict) -> str:
    to_endcode = data.copy()
    exp = timezone.utc() + timedelta(minutes=expair_min)
    to_endcode.update({"exp": exp})
    token = jwt.encode(to_endcode, secret_key, algorithm=algo)
    return token