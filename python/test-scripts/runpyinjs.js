// testing some shiet

console.log("testing!");

var python = require('child_process').spawn(
     'python',
     // second argument is array of parameters, e.g.:
     ["test.py"]
);