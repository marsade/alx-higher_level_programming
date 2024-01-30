#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
if (args.length > 1) {
  console.log('Usage: ./0-readme.js URL');
} else {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  request(url + args[0], function (error, res, body) {
    if (error) {
      console.log(error);
    } else {
      const charArr = JSON.parse(body).characters;
      charArr.forEach(element => {
        request(element, function (err, res, body) {
          if (err) {
            console.log(err);
          } else {
            const char = JSON.parse(body).name;
            console.log(char);
          }
        });
      });
    }
  });
}
