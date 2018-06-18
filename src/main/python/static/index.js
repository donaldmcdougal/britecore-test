$(document).ready(() => {
  const vm = new IndexViewModel();

  // This stuff is for getting all the initial data.
  const clientModule = new ClientModule();
  const productAreaModule = new ProductAreaModule();
  const featureRequestModule = new FeatureRequestModule();
  // because this is a simple project, we won't bother trying to solve callback hell.
  // but if we wanted to, we could use promises to mitigate that.
  clientModule.getAll((clientsData) => {
    for (let i = 0, j = clientsData.length; i < j; i++) {
      vm.clients.push(clientsData[i]);
      vm.clientMap[clientsData[i].id] = clientsData[i];
    }
    productAreaModule.getAll((productAreaData) => {
      for (let i = 0, j = productAreaData.length; i < j; i++) {
        vm.productAreas.push(productAreaData[i]);
        vm.productAreaMap[productAreaData[i].id] = productAreaData[i];
      }
      featureRequestModule.getAll((featureRequestData) => {
        for (let i = 0, j = featureRequestData.length; i < j; i++) {
          let d = Date.parse(featureRequestData[i].target_date);
          d = new Date(d);
          d = d.toISOString();
          d = d.substr(0, 10);
          featureRequestData[i].target_date = d;
          vm.featureRequests.push(featureRequestData[i]);
        }
      });
    });
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
