#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (char) {
    if (char === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(`${char}`.repeat(this.width));
      }
    }
  }
};
