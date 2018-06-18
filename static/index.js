$(document).ready(() => {
  const vm = new IndexViewModel();

  // This stuff is for getting all the initial data.
  const clientModule = new ClientModule();
  const productAreaModule = new ProductAreaModule();
  const featureRequestModule = new FeatureRequestModule();
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
  featureRequestModule.getAll((featureRequestData) => {
    for (let i = 0, j = featureRequestData.length; i < j; i++) {
      vm.featureRequests.push(featureRequestData[i]);
    }
  });

  ko.bindingHandlers.modal = {
    init: function(element, valueAccessor) {
      $(element).modal({
        show: false
      });
      const value = valueAccessor();
      if (ko.isObservable(value)) {
        $(element).on('hidden.bs.modal', () => {
          value(false);
        });
      }
    },
    update: function(element, valueAccessor) {
        const value = valueAccessor();
        if (ko.utils.unwrapObservable(value)) {
          $(element).modal('show');
        } else {
          $(element).modal('hide');
        }
    }
  };

  ko.applyBindings(vm);
});
