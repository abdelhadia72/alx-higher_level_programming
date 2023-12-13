#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, currentElement) {
    return currentElement === searchElement ? count + 1 : count;
  }, 0);
};
