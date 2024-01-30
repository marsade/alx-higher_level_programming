#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');
if (args.length > 1) {
  console.log('Usage: ./0-readme.js URL');
} else {
  req.get(process.argv[2]).on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
}
