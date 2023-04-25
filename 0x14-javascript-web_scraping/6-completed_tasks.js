#!/usr/bin/node
// computes the number of tasks completed by user id
// first argument is the API URL

const request = require('request');

const url = process.argv[2];
const tasksCount = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    // iterate through tasks and check if task is completed then increase its count
    data.forEach((task) => {
      if (task.completed) {
        tasksCount[task.userId] += 1;
      }
    });
    console.log(tasksCount);
  } else {
    console.log(error);
  }
});
