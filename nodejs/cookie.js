const http = require('http');

http
  .createServer((req, res) => {
    console.log(req.url, req.headers.cookie);
    //Set-Cookie는 브라우저한테 다음과 같은 값의 쿠키를 저장하라는 의미
    res.writeHead(200, { 'Set-Cookie': 'mycookie=test' });
    res.end('Hello world');
  })
  .listen(8080, () => {
    console.log('server run');
  });
