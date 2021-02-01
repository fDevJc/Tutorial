const http = require('http');
const fs = require('fs').promises;

const users = {};

http
  .createServer(async (req, res) => {
    //server run
    try {
      console.log(req.method + ' // ' + req.url);
      if (req.method === 'GET') {
        //GET
        if (req.url === '/') {
          const data = await fs.readFile('./jcFront.html');
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
          return res.end(data);
        } else if (req.url === '/users') {
          res.writeHead(200, {
            'Content-Type': 'application/json; charset=utf-8',
          });
          return res.end(JSON.stringify(users));
        }
        // js , html ....
        try {
          const data = await fs.readFile(`.${req.url}`);
          return res.end(data);
        } catch (err) {
          //
        }
      } else if (req.method === 'POST') {
        //POST
        if (req.url === '/user') {
          //response
          let body = '';
          req.on('data', (data) => {
            body += data;
          });
          return req.on('end', () => {
            console.log('POST BODY : ', body);
            const { name } = JSON.parse(body);
            const id = Date.now();
            users[id] = name;
            res.writeHead(201, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end('ok');
          });
        }
      } else if (req.method === 'DELETE') {
        //DELETE
      } else if (req.method === 'PUT') {
        //PUT
      }
      res.writeHead(404);
      return res.end('NOT FOUND');
    } catch (err) {
      console.log(err);
    }
  })
  .listen(8080, () => {
    console.log('port:8080 server running.....');
  });
