const { odd, even } = require("./var");

function checkOddorEven(num) {
  if (num % 2 == 0) {
    return even;
  } else {
    return odd;
  }
}

module.exports = checkOddorEven;
