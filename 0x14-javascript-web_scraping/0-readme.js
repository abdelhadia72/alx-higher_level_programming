#!/usr/bin/node
/*
 * print out the conant
 * of the file in the argment
 * the first argment
 */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
