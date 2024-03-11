#!/usr/bin/node
const { argv } = require('node:process');
const numbers = argv.slice(2);
// numbers.forEach(number => parseInt(number))
numbers.sort((a, b) => b - a);
console.log(numbers[1]);
