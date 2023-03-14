#!/usr/bin/node

/*
 * increments and calls a function.
 * increments and calls a function.
 */
exports.addMeMaybe = function (number, theFunction) {
  if (typeof theFunction == 'function') {
    theFunction.call(this, number + 1);
  }
};
