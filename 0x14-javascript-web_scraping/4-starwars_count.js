#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
if (args.length > 1) {
  console.log('Usage: ./0-readme.js URL');
} else {
  const url = args[0];
  request(url, function (error, res, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body).results;
      console.log(films.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0));
    }
  });
}
