#!/usr/bin/node
const { argv } = require('node:process');
const x = parseInt(argv[2]);
if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurences');
