#!/usr/bin/node
/* fetch all user for a specific 
 * move based on the id 
 */

const request = require('request');
const base = 'https://swapi-api.alx-tools.com/api/'

if (process.argv.length < 3){
    console.error(`Usage: ./${process.argv[1]} <ID>`)
}

