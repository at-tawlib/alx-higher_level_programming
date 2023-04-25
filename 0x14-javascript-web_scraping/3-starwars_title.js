#!/usr/bin/node
// prints the title of a Star Wars movie with the episode number
// first argument is movie ID

const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];
const url = endpoint + '/' + id;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const json = JSON.parse(body);
    console.log(json.title);
  } else {
    console.log(error);
  }
});
