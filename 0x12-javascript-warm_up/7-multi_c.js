#!/usr/bin/node

const numOfLoops = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOfLoops; i++) {
    console.log('C is fun');
  }
}
