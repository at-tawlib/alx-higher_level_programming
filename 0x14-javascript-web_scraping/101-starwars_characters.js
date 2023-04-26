#!/usr/bin/node
// prints all characters of a Star Wars movie
// first argument is movie ID
// display characters in the same order in the film response

const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];
const url = endpoint + '/' + movieId;
let characters = [];

// get characters into an array
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    characters = JSON.parse(body).characters;
    showCharacters(0);
  } else {
    console.log(error);
  }
});

// get the character at the index
const showCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const name = JSON.parse(body).name;
      console.log(name);
      showCharacters(index + 1);
    }
  });
};
