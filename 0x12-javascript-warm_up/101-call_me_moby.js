#!/usr/bin/node

/*
 * has a function that executes x times a function
 * function must be visible from outside
 */
exports.callMeMoby = function (x, theFunction) {
  if (isNaN(Number(x))) {
    return NaN;
  }
  while (x > 0) {
    if (typeof theFunction === 'function') {
      theFunction.call();
      --x;
    } else {
      return;
    }
  }
};
