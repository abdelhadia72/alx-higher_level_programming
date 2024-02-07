#!/usr/bin/node
/* fetch all user for a specific
 * move based on the id
 */

const request = require('request');
const base = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length < 3) {
  console.error(`Usage: ./${process.argv[1]} <ID>`);
}

const movieUrl = `${base}films/${process.argv[2]}`;
request.get(movieUrl, (err, res) => {
  if (err) {
    console.error('Error:', err.message);
  }

  const data = JSON.parse(res.body).characters;

  const ids = data.map((char) => {
    const id = (char.split('/'))[(char.split('/').length - 2)];
    return id;
  });

  console.log("start");
  ids.forEach((id) => {
    const charactersId = `${base}people/${id}`;
    request.get(charactersId, (err, res) => {
      if (err) {
        console.error('Error:', err.message);
      }
      // console.log(JSON.parse(res.body).name);
      console.log("fetching");
    });
    console.log("me");
  });
  console.log("end");
});
