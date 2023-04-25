#!/usr/bin/node
// writes a string to a file
// first argument is file path
// second argument is the string to write

const fs = require('fs');

const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, err => {
  if (err) {
    console.log(err);
  }
});
