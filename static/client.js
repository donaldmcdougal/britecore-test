'use strict';

class Client extends IdName {
  constructor(id, name) {
    super(id, name);
  }
}

class ClientModule {

  constructor() {}

  getAll(cb) {
    $.get('/client', (data) => {
      const clients = [];
      for (const c in data) {
        clients.push(new Client(c.id, c.name));
      }
      cb(clients);
    });
  }
}
