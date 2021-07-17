var http = require('http');
 
http.createServer(function(request, response){
    response.end("200");
}).listen(8000);