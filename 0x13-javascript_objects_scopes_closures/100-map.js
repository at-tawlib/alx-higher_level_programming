#!/usr/bin/node

/*
 * imports an array and computes a new array.
 * import list from the file 100-data.js
 * A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
 */

const list = require('./100-data.js').list;

const newList = list.map((val, idx) => val * idx);
console.log(list);
console.log(newList);
