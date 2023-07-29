npm init -y

// MERN
// Mongo, Express, React, Node
// npm - node pkg manager
// fs - inbuilt file package
// Install express package
// mpm install express

//queryparameter
// /route?param1&param2
// req.query.param1
// req.query.param2

// req.header.param1

// via body  , type JSON
// {
//    "param1": "value1"
// }
// req.body.param1 XXXXXX Body is not available directly
// req.body is undefined ... I don't know body is of which type .. here JSON
// req.body does not come out of box
// have to install 3rd party library let say here for JSON
// npm install body-parser
// var bodyParser = require("body-parser")
// app.use(bodyParser.json()) // middleware
// now do req.body or req.body.param1 , will show the entire json

// app.use(middleware)
// function middleware(req, resp, next)
// next() call will move you to route or error before calling route
