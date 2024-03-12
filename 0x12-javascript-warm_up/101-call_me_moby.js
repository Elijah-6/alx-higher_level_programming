#!/usr/bin/node
const callMeMoby = (number, callBack) => {
    for(let i = 0; i < number; i++) {
        callBack();
}
}

exports.callMeMoby = callMeMoby;