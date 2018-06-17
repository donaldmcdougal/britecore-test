'use strict';

class ProductArea extends IdName {
  constructor(id, name) {
    super(id, name);
  }
}

class ProductAreaModule {

  constructor() {}

  getAll(cb) {
    $.get('/product_area', (data) => {
      /*
      const pas = [];
      for (const c in data) {
        pas.push(new ProductArea(c.id, c.name));
      }
      cb(pas);
      */
      cb(data);
    });
  }
}
