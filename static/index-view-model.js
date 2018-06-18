class IndexViewModel {
  constructor() {
    var self = this;
    self.selectedClient = ko.observable();
    self.selectedProductArea = ko.observable();
    self.selectedFeatureRequest = ko.observable();
    self.clients = ko.observableArray();
    self.productAreas = ko.observableArray();
    self.featureRequests = ko.observableArray();

    self.deleteFeatureRequest = (data, event) => {
      var frm = new FeatureRequestModule();
      frm.remove(data.id, (err, rsp) => {
        if (err) {
          alert(err);
        } else {
          if (rsp === true) {
            self.featureRequests.remove(data);
          } else {
            alert('Unexpected server output when deleting feature request.');
          }
        }
      });
    };
  }
}
