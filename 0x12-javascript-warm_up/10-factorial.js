#!/usr/bin/node

/**
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 */
function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const c = process.argv[2];
if (isNaN(c)) {
  console.log(1);
} else {
  console.log(factorial(c));
}
