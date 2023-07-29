const express = require('express')
const app = express()
const port = 3000

var bodyParser = require("body-parser")
app.use(bodyParser.json()) // act as middleware

function handleRequestHome(req, res){
    res.send("Hello World")
}

app.get('/', handleRequestHome)

function started() {
    console.log(`Example app listening on port ${port}`)
}
app.listen(port, started)


function calculateSum(counter){
    var sum = 0;
    for (var i=1; i <= counter; i++){
        sum += i;
    }
    return sum
}

function handleCalculateSum(req, res) {
    var counter = req.query.counter
    res.send("Sum is: " + calculateSum(counter))
}

app.get("/calculateSum", handleCalculateSum)

// var ans = calculateSum(100);
// console.log(ans);

// const fs = require("fs");

// function cb(err, data){
//     console.log(data);
// }

// fs.readFile("readme.txt", "utf-8", cb); // async call using callback
// console.log("readfile");


