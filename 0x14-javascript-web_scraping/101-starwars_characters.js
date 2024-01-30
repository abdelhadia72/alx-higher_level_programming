#!/usr/bin/node
/* fetch all user for a specific
 * movie based on the id and printed
 * by order
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
    console.log(ids)

    const idList = [];
    let completedRequests = 0;
    ids.forEach((id) => {
        const charactersId = `${base}people/${id}`;
        request.get(charactersId, (err, res) => {
            if (err) {
                console.error('Error:', err.message);
            }
            // idList.push(JSON.parse(res.body).name);
            // completedRequests++;
            // if (completedRequests === ids.length) {
            //     console.log(idList.sort().reverse());
            // }
            console.log(JSON.parse(res.body).name);
        });
    });
});
