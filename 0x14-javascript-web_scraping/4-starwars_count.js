#!/usr/bin/node
//  prints the number of movies where the character “Wedge Antilles” is present
// first argument is the API URL
// NB: actor id of Wedge Antilles is 18

const request = require('request');

const url = process.argv[2];
const characterId = '18';
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/' + characterId + '/';
let count = 0;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const json = JSON.parse(body);
    // get films
    const films = json.results;
    films.forEach((film) => {
      // get characters of films
      const characters = film.characters;
      characters.forEach((character) => {
        if (character === characterUrl) {
          count++;
        }
      });
    });

    console.log(count);
  } else {
    console.log(error);
  }
});
