#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
    number++;
    theFunction(number);
}
exports.addMeMaybe = addMeMaybe;