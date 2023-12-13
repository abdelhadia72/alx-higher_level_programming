#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length <= 1) {
    return list;
  }
  const reversedRest = exports.esrever(list.slice(1));
  return reversedRest.concat(list[0]);
};
