#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, element) {
    return count + (element === searchElement);
  }, 0);
};
