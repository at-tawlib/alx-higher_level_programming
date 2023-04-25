#!/usr/bin/node
// computes the number of tasks completed by user id
// first argument is the API URL

const request = require('request');

const url = process.argv[2];
const tasksCount = {};

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    // iterate through tasks and check if task is completed then increase its count
    data.forEach((task) => {
      if (task.completed) {
        if (!tasksCount[task.userId]) {
          tasksCount[task.userId] = 1;
        } else {
          tasksCount[task.userId] += 1;
        }
      }
    });
    console.log(tasksCount);
  } else {
    console.log(error);
  }
});
