#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
// first argument is URL
// second argument is the file path

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, err => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
