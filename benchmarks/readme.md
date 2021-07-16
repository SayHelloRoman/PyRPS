# Benchmarks that PyRPS showed us
```
python PyRPS.py -url http://127.0.0.1:8000 -time 5
```

## http

```
node http_server.js
```

```
5539 RPS in 5 seconds
1107 RPS in second
```


## express
```
npm i express
node express_server.js
```

```
5182 RPS in 5 seconds
1036 RPS in second
```

## fastapi
```
pip install fastapi
pip install uvicorn
python fastapi_server.py
```

```
3102 RPS in 5 seconds
620 RPS in second
```

## flask
```
pip install flask
python flask_server.py
```

```
3327 RPS in 5 seconds
665 RPS in second
```

## aiohttp
```
pip install aiohttp
python aiohttp_server.py
```

```
4956 RPS in 5 seconds
991 RPS in second
```