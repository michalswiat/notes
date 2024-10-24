## Frontend

### Node.js

It is using to write frontend code in javescript or typescript (with additional packets)

Getting started:
- install node.js (go to node.js site and use curl)
- it is recommended to use node version manager to easily switch between node.js versions (ex. nvm-sg, look at github)
- check if node.js is installed correctly
    * $node -v
    * &npm -v

### Pure node.js webserver

The simplest example of node.js use is running the web server.
```
Example code block can be found on official node.js web
```

**Parsing varaible in strings**
```
console.log(`Server running at http://${hostname}:${port}/`);
```
It is important to use ` not '.

The server from example can't be reached. To check connectivite the serverhere application can be used.

$npm install serverhere

$serverhere --port 3000 public

$npm install && npm start

If the server is running instide virtual machine the port redirection should be set to allow access via localhost (3000 => 3000).

**Can't reach 127.0.0.1**

It is possible that the specific localhost address can't be reached from the host when the server is running inside virtual machine. To fix that use localhost. It can be done by passing only port attribute to server listen method:
```
server.listen(PORT, () => {
    console.log('running');
});
```

**Create server**

There are many options to create server with node.js.
```
const { createServer } = require('node:http'); //for package manager

const server = createServer((req, res) => {
    //modify response here, or check request
});

server.listen(()=> {
    //log sth
});
```

or http can be used directly:
```
const http = require('http');

const server = http.createServer((req, res) => {

});

server.listen(() => {

});
```
Response creation is really simple. Any html file can be read and returned as response. Different response code can be returned based on the code flow. Example code to look for index.html file and returning error code when sth went wrong:
```
import { createServer } from 'http'
import path from 'path';
import fs from 'fs'

const server = createServer((res, req) => {
    const filePath = path.join(__dirname, 'index.html');
    if (req === '/') {
        // using setHeader method
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello world')

        // also index.html can be read from the file here and returned in a html content
        fs.readFile(fp, (err, data) => {
            res.statusCode = 200;
            res.setHeader('Content-Type', 'text/html');
            res.end(data);
        });
    } else {
        // using writeHead method
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 - not found');
    }
});
```
For java script file application/javascript content type can be used. Web browser is requesting file when reaching <script> tag with file name,

**type-script**

The same server file example using type-script:
```
import { IncomingMessage, ServerResponse, createServer } from 'http'
import * as path from 'path';
import * as fs from 'fs'; //Fix some import issue using this * as construction

const server = createServer((res: ServerResponse, req: IncomingMessage) => {
    const filePath = path.join(__dirname, 'index.html');
    if (req === '/') {
        // using setHeader method
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello world')

        // also index.html can be read from the file here and returned in a html content
        fs.readFile(fp, (err, data) => {
            res.statusCode = 200;
            res.setHeader('Content-Type', 'text/html');
            res.end(data);
        });
    } else {
        // using writeHead method
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 - not founf');
    }
});
```
It needs some env preparation to work (solve the includes, creating tsconfig.js etc.)

$npm init -y

$npm install typescript ts-node @types/node --save-dev

$npx tsc --init