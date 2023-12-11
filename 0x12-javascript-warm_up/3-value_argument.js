#!/usr/bin/node

if (process.argv.length > 2) {
  for (let i = 2; i < process.argv.length; i++) {
    console.log(process.argv[i]);
  }
} else {
  console.log('No argument');
}
