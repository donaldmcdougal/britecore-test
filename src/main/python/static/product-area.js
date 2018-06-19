'use strict';

class ProductAreaModule {

  constructor() {}

  getAll(cb) {
    $.get('/product_area', (data) => {
      cb(data);
    });
  }
}
