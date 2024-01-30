#!/usr/bin/node
/* send response and print
 * out status code using the 'request' module
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log(`Usage: ./${process.argv[1]} <URL>`);
  process.exit(1);
}

const url = process.argv[2];

request(url, (response) => {
  console.log(response.statusCode);
});
