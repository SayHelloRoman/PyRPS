const http_server = require("benchmarks/http_server");
 
http_server.createServer(function(request, response){
    response.end("200");
}).listen(8000);