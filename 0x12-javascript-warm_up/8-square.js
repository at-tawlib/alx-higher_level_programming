#!/usr/bin/node

/*
 * prints a square
 * if the first argument can't be converted to an integer, print "Missing size"
 * use X to print the square
 */
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
