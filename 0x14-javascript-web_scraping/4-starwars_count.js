#!/usr/bin/node
/* count how many movies where the character
 * “Wedge Antilles” is present.
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log(`Usage: ./${process.argv[1]} <URL>`);
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) {
    console.error('Error: ', err.message);
    process.exit(1);
  }
  const data = JSON.parse(res.body).results;

  const result = data
    .map((char) => char.characters)
    .flat()
    .filter((url) => url.includes('18'));

  const len = result.length;
  console.log(len);
});
