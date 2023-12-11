#!/usr/bin/node

const numOfLoops = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numOfLoops; ++i) {
    console.log(('x').repeat(numOfLoops));
  }
}
