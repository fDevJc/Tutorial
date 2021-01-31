const http = require('http');
const fs = require('fs').promises;

const users = [];

http
  .createServer(async (req, res) => {
    try {
      console.log('>>req.method :', req.method, ' , req.url :', req.url);
      if (req.method === 'GET') {
        if (req.url === '/') {
          const page = await fs.readFile('./jcFront.html');
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
          return res.end(page);
        }

        try {
          const data = await fs.readFile(`.${req.url}`);
          return res.end(data);
        } catch (err) {
          //
        }
      } else if (req.method === 'POST') {
        if (req.url === '/user') {
          let body = '';
          req.on('data', (data) => {
            body += data;
          });
          req.on('end', () => {
            //
            console.log('>>>body :', body);
            const { user } = JSON.parse(body, (key, value) => {
              console.log('>>>key,value :', key, value);
            });
            //console.log('>>>user.name :', user.name);
            users.push(user);
            console.log('>>>users:', users);
            res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end('ok');
          });
        }
      }
    } catch (err) {
      console.error(err);
    }
  })
  .listen(8080, () => {
    console.log('8080 port ready');
  });
