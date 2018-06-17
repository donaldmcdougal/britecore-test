class IndexViewModel {
  constructor(clients, productAreas) {
    var self = this;
    self.selectedClient = ko.observable();
    self.selectedProductArea = ko.observable();
    self.clients = ko.observableArray();
    for (let i = 0, j = clients.length; i < j; i++) {
        self.clients.push(clients[i]);
    }
    self.productAreas = ko.observableArray();
    for (let i = 0, j = productAreas.length; i < j; i++) {
      self.productAreas.push(productAreas[i]);
    }
  }
}

$(document).ready(() => {
  const clientModule = new ClientModule();
  const productAreaModule = new ProductAreaModule();
  clientModule.getAll((clientsData) => {
    productAreaModule.getAll((productAreaData) => {
      const vm = new IndexViewModel(clientsData, productAreaData);
      ko.applyBindings(vm);
    });
  });
});
