#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const id = dict[key];

  if (!(id in newDict)) {
    newDict[id] = [];
  }
  newDict[id].push(key);
}
console.log(newDict);
