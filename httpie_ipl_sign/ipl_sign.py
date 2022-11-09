import hashlib
import hmac
from typing import Any, Optional

from httpie.plugins import AuthPlugin
from requests import PreparedRequest
from requests.auth import AuthBase


__version__ = '1.0.0'
__author__ = 'Valentin Nagorny'
__licence__ = 'MIT'


def hmac_sign(
        data: bytes,
        secret: bytes,
        salt: Optional[bytes] = None,
        counter: Optional[int] = None,
) -> str:
    if salt is not None:
        data = salt + b'$' + data
    if counter is not None:
        data = str(counter).encode() + b'$' + data
    return hmac.new(
        key=secret, msg=data, digestmod=hashlib.sha256
    ).hexdigest()


class HTTPIplSignAuth(AuthBase):
    def __init__(
            self,
            key: Optional[str] = None,
            secret: Optional[str] = None
    ) -> None:
        self.key = key
        self.secret = secret

    def __eq__(self, other: Any) -> bool:
        return all([
            self.key == getattr(other, 'key', None),
            self.secret == getattr(other, 'secret', None),
        ])

    def __ne__(self, other: Any):
        return not self == other

    def __call__(self, r: PreparedRequest):
        sign = None
        if self.secret is not None:
            sign = hmac_sign(r.body, self.secret.encode('utf-8'))
        r.prepare_url(
            r.url, {'api_key': self.key, 'sign': sign}
        )
        return r


class IplSignPlugin(AuthPlugin):
    name = 'Ipl request body sign'
    auth_type = 'ipl-sign'
    auth_require = False
    description = ''

    def get_auth(
            self,
            username: Optional[str] = None,
            password: Optional[str] = None,
    ) -> AuthBase:
        return HTTPIplSignAuth(username, password)
