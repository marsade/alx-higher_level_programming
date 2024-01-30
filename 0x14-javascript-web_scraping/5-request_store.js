#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length > 2) {
  console.log('Usage: ./0-readme.js URL');
} else {
  const request = require('request');
  const fs = require('fs');
  const url = args[0];
  request.get(url, function (err, response) {
    if (err) {
      console.log(err);
    } else {
      const res = response.body;
      fs.writeFile(args[1], res, (err) => {
        if (err) throw err;
      });
    }
  });
}
