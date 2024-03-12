#!/usr/bin/node
const { argv } = require('node:process');
const numbers = argv.slice(2).map(Number);
if (numbers.length <= 1) {
  console.log(0);
} else {
  const uniqueNumbers = [...new Set(numbers)]; // Remove duplicates
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a); // Sort in descending order
  console.log(sortedNumbers[1]);
}
