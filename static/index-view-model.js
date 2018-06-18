class IndexViewModel {
  constructor() {
    var self = this;
    self.selectedClient = ko.observable();
    self.selectedProductArea = ko.observable();
    self.selectedFeatureRequest = ko.observable();
    self.clients = ko.observableArray();
    self.productAreas = ko.observableArray();
    self.featureRequests = ko.observableArray();

    var frm = new FeatureRequestModule();

    self.deleteFeatureRequest = (data, event) => {
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

    self.updateFeatureRequest = (data, event) => {
      console.log(data);
      frm.update(data, (err, response) => {
        if (err) {
          alert(err);
        } else if (response) {
          for (let fr in self.featureRequests) {
            if (fr.id === data.id) {
              self.featureRequests.replace(fr, data);
              break;
            }
          }
          alert('Feature Request Updated.');
        } else {
          alert('Unexpected server error when updating feature request.');
        }
      });
    };
  }
}
