#!/usr/bin/node

// prints a message depending of the number of arguments passed
// If only one argument is passed to the script, print “Argument found”
// Otherwise, print “Arguments found”
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
