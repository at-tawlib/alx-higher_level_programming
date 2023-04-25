#!/usr/bin/node
// displays the status code of a GET request
// first argument is URL to the request

const request = require('request');

const url = process.argv[2];
request(url).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
