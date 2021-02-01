const http = require('http');
const fs = require('fs').promises;

const users = {};

http
  .createServer(async (req, res) => {
    console.log(req.method, ' , ', req.url);
    try {
      if (req.method === 'GET') {
        if (req.url === '/') {
          //
          const page = await fs.readFile('./jcFront2.html');
          res.writeHead(200, { 'Content-Type': 'text/html charset=utf-8' });
          return res.end(page);
        } else if (req.url === '/users') {
          const data = JSON.stringify(users);
          res.writeHead(200, {
            'Content-Type': 'application/json charset=utf-8',
          });
          console.log('GET:/users data', data);
          return res.end(data);
        }

        try {
          const page = await fs.readFile(`.${req.url}`);
          res.writeHead(200, { 'Content-Type': 'text/html charset=utf-8' });
          return res.end(page);
        } catch (err) {
          console.log(err);
        }
      } else if (req.method === 'POST') {
        if (req.url === '/user') {
          let body = '';
          req.on('data', (data) => {
            body += data;
          });
          req.on('end', () => {
            const id = Date.now();
            console.log('POST:/user body', body);
            const user = JSON.parse(body);
            console.log('POST:/user user', user);
            users[id] = user;
          });
          res.writeHead(201, { 'Content-Type': 'text/html charset=utf-8' });
          return res.end('ok');
        }
      }
    } catch (err) {
      console.log(err);
    }
  })
  .listen(8080, () => {
    console.log('port: 8080 server run');
  });
