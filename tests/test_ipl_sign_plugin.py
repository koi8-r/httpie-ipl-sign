from requests import Request

from httpie_ipl_sign.ipl_sign import IplSignPlugin


def test_ipl_sign_plugin() -> None:
    auth = IplSignPlugin().get_auth('iam', 'secret')
    req = Request(method='GET', url='http://localhost?a=b').prepare()
    peq = auth.__call__(req)
    assert (
        'https://localhost/?a=b'
        '&api_key=iam&sign='
        'f9e66e179b6747ae54108f82f8ade8b3c25d76fd30afde6c395822c530196169',
        peq.url,
    )
