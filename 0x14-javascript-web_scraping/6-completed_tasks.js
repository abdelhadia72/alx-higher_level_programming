#!/usr/bin/node
/* print user withe there
 * complted tasks
 */

const request = require('request');

if (process.argv.length < 3) {
  console.error(`Usage: ./${process.argv[1]} <URL>`);
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) {
    console.error('Error:', err.message);
  }
  const taskObj = {};
  const data = JSON.parse(res.body);
  data.map((obj) => {
    if (!(taskObj[`${obj.userId}`])) { taskObj[`${obj.userId}`] = 0; }
    if (obj.completed) { taskObj[`${obj.userId}`] = taskObj[`${obj.userId}`] + 1; }
    return taskObj;
  });
  console.log(taskObj);
});
