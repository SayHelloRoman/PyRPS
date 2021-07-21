# Benchmarks that PyRPS showed us
```
python PyRPS.py -url http://127.0.0.1:8000 -time 5
```

## http.js

```
node http_server.js
```

```
Total requests: 13040
RPS           : 2608
```


## express.js
```
npm i express
node express_server.js
```

```
Total requests: 13720
RPS           : 2744
```

## fastapi.py
```
pip install fastapi
pip install uvicorn
python fastapi_server.py
```

```
Total requests: 6723
RPS           : 1344
```

## flask.py
```
pip install flask
python flask_server.py
```

```
Total requests: 4480
RPS           : 896
```

## aiohttp.py
```
pip install aiohttp
python aiohttp_server.py
```

```
Total requests: 11119
RPS           : 2223
```

## http.go
```
go run http_server.go
```

```
Total requests: 13640
RPS           : 2728
```

## Socket.java
```
javac SocketServer.java
java SocketServer
```

```
Total requests: 5560
RPS           : 1112
```