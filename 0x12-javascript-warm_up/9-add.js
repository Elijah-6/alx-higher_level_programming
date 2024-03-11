#!/usr/bin/node
const { argv } = require('node:process');
const firstNum = parseInt(argv[2], 10);
const secondNum = parseInt(argv[3], 10);

console.log(add(firstNum, secondNum));

function add (a, b) {
  return a + b;
}
