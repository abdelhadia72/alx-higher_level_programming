#!/usr/bin/node

const numOfLoops = parseInt(process.argv[2]);
if (parseInt(process.argv[2])) {
  for (let i = 0; i < numOfLoops; i++) {
    console.log(('X').repeat(numOfLoops));
  }
} else {
  console.log('Missing size');
}
