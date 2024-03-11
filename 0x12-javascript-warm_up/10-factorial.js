#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
console.log(factorial(number));

function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    let result = 1;
    for (let i = 1; i <= num; i++) {
      result *= i;
    }
    return result;
  }
}
