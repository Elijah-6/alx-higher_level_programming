#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
console.log(factorial(number));

function factorial (num) {
  if (num === 0 || !num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
