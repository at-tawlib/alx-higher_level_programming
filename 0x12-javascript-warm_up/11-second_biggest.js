#!/usr/bin/node

/*
 * script that searches the second biggest integer in the list of arguments
 * print 0 if no argument is passed
 * if number of arguments is 1, print 0
 */

function secondBiggest () {
  if (!arguments[0] || arguments[0].length <= 1) {
    return 0;
  }

  arguments[0].splice(arguments[0].indexOf(String(Math.max(...arguments[0]))), 1);
  return Math.max(...arguments[0]);
}

console.log(secondBiggest(process.argv.slice(2)));
