#!/usr/bin/node

const number = process.argv[2];

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const result = factorial(number);
console.log(result);
