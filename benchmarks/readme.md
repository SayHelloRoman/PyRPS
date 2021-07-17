# Benchmarks that PyRPS showed us
```
python PyRPS.py -url http://127.0.0.1:8000 -time 5
```

## http.js

```
node http_server.js
```

```
13040 RPS in 5 seconds
2608 RPS in second
```


## express.js
```
npm i express
node express_server.js
```

```
13720 RPS in 5 seconds
2744 RPS in second
```

## fastapi.py
```
pip install fastapi
pip install uvicorn
python fastapi_server.py
```

```
5387 RPS in 5 seconds
1077 RPS in second
```

## flask.py
```
pip install flask
python flask_server.py
```

```
4480 RPS in 5 seconds
896 RPS in second
```

## aiohttp.py
```
pip install aiohttp
python aiohttp_server.py
```

```
11119 RPS in 5 seconds
2223 RPS in second
```

## http.go
```
go run http_server.go
```

```
13640 RPS in 5 seconds
2728 RPS in second
```

## Socket.java
```
javac SocketServer.java
java SocketServer
```

```
5560 RPS in 5 seconds
1112 RPS in second
```