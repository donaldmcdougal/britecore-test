class IndexViewModel {
  constructor() {
    var self = this;
    self.selectedClient = ko.observable();
    self.selectedProductArea = ko.observable();
    self.selectedFeatureRequest = ko.observable();
    self.clients = ko.observableArray();
    self.productAreas = ko.observableArray();
    self.featureRequests = ko.observableArray();
  }
}

$(document).ready(() => {
  const clientModule = new ClientModule();
  const productAreaModule = new ProductAreaModule();
  const vm = new IndexViewModel();
  clientModule.getAll((clientsData) => {
    for (let i = 0, j = clientsData.length; i < j; i++) {
      vm.clients.push(clientsData[i]);
    }
  });
  productAreaModule.getAll((productAreaData) => {
    for (let i = 0, j = productAreaData.length; i < j; i++) {
      vm.productAreas.push(productAreaData[i]);
    }
  });
  ko.applyBindings(vm);
});
