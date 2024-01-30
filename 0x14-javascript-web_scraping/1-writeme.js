#!/usr/bin/node
/*
 * javascript code that write the
 * the cotant you pass in argv 3 into
 * a file name <argv[2]>.txt
 */

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) { console.log(err); }
});
