"""Local teaching scaffold with a deterministic backend; no production security claim."""
import hmac
import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, ConfigDict, Field, field_validator
from brewbyte import fixture_summary, retrieve

app = FastAPI(title='BrewByte local teaching API')


class Request(BaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str = Field(min_length=1, max_length=4000)

    @field_validator('text')
    @classmethod
    def nonblank(cls, value):
        if not value.strip():
            raise ValueError('Nonblank text required')
        return value.strip()


def identity(authorization):
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(401, 'Bearer credential required')
    token = authorization[7:]
    # Distinct configured tokens bind roles. Roles cannot be supplied in user text.
    for env, role in [('BREWBYTE_MANAGER_TOKEN','manager'), ('BREWBYTE_STAFF_TOKEN','staff')]:
        expected = os.environ.get(env)
        if expected and hmac.compare_digest(token.encode(), expected.encode()):
            return role
    raise HTTPException(403, 'Access denied')


@app.get('/health')
def health():
    return {'status': 'ok', 'backend': 'deterministic-fixture', 'live_model': False}


@app.post('/summary')
def summary(request: Request, authorization: str | None = Header(default=None)):
    identity(authorization)
    return fixture_summary(request.text)


@app.post('/policy')
def policy(request: Request, authorization: str | None = Header(default=None)):
    role = identity(authorization)
    return {'role': role, 'backend': 'lexical-baseline', 'sources': retrieve(request.text, role)}
