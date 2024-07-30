#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]),{
    flags: 'a',
    encoding: 'utf8'
});
