#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length > 2) {
  console.log('Usage: ./0-readme.js <string>');
} else {
  const fs = require('fs');
  const string = args[1];
  fs.writeFile(args[0], string, (err) => {
    if (err) throw err;
  });
}
