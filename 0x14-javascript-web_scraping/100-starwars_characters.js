#!/usr/bin/node
// prints all characters of a Star Wars movie
// first argument is movie ID

const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];
const url = endpoint + '/' + movieId;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // get the characters in the movie
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      // get the name of each character
      request(character, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  } else {
    console.log(error);
  }
});
