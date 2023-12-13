#!/usr/bin/node

let gvar = 0;
exports.logMe = function (item) {
  console.log(`${gvar++}: ${item}`);
};
