from fastapi.security import OAuth2PasswordBearer

SECURITY_SCHEME = OAuth2PasswordBearer(tokenUrl="auth/login")
