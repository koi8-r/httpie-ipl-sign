## Adds `api_key` and hmac `sign` to parameters of a query string

### Install httpie
```shell
# Examples
apt install httpie
brew install httpie
pip install httpie
```

### Install plugin
```shell
httpie cli plugins install \
  https://github.com/koi8-r/httpie-ipl-sign/raw/master/dist/httpie_ipl_sign-1.0.0-py3-none-any.whl
# or directly from https://github.com/koi8-r/httpie-ipl-sign/archive/refs/heads/master.zip
```

### Use
```shell
http -v -A ipl-sign -a key:secret api.example.org
```
