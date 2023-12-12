#!/usr/bin/node

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

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
