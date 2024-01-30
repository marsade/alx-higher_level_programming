#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length > 1) {
  console.log('Usage: ./0-readme.js <string>');
} else {
  const fs = require('fs');
  fs.readFile(args[0], (err, inputD) => {
    if (err) throw err;
      console.log(inputD.toString());
  })
}
