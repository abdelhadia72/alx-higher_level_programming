#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    this.width = w > 0 ? w : undefined;
    this.height = h > 0 ? h : undefined;
  }
}
