#!/usr/bin/node

// prints the first argument passed to it
// if no arguments passed, print "No argument"
const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
