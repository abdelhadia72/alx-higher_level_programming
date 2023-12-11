#!/usr/bin/node

const num = Math.floor(process.argv[2]);
if (Number.isInteger(num)) {
  console.log(num);
} else {
  console.log('Not a number');
}
