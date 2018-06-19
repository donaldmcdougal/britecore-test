'use strict';

class ClientModule {

  constructor() {}

  getAll(cb) {
    $.get('/client', (data) => {
      cb(data);
    });
  }
}
