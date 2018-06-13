let clients = [];
let productAreas = [];
let viewModel;

$(document).ready(() => {
  const clientModule = new ClientModule();
  const productAreaModule = new ProductAreaModule();
  clientModule.getAll((data) => {
    clients = data;
    productAreaModule.getAll((data) => {
      productAreas = data;
    });
    viewModel = {
      clients: ko.observableArray(clients),
      productAreas: ko.observableArray(productAreas)
    };
    selectedClient: ko.observable();
    selectedProductArea: ko.observable();
    ko.applyBindings(viewModel);
  });
});
