class IndexViewModel {
  constructor() {
    var self = this;
    self.selectedClient = ko.observable();
    self.selectedProductArea = ko.observable();
    self.selectedFeatureRequest = ko.observable();
    self.newFeatureRequest = ko.observable();
    self.clients = ko.observableArray();
    self.productAreas = ko.observableArray();
    self.featureRequests = ko.observableArray();

    self.clientMap = {};
    self.productAreaMap = {};

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
      frm.update(data, (err, response) => {
        if (err) {
          alert(err);
        } else if (response) {
          var data = self.featureRequests().slice(0);
          self.featureRequests([]);
          self.featureRequests(data);
          $('.modal').modal('hide');
        } else {
          alert('Unexpected server error when updating feature request.');
        }
      });
    };

    self.createFeatureRequest = (data, event) => {
      frm.create(data, (err, response) => {
        if (err) {
          alert(err);
        } else if (response) {
          response.target_date = new Date(Date.parse(response.target_date)).toISOString().substr(0, 10);
          self.featureRequests.push(response);
          self.newFeatureRequest({
            title: '',
            description: '',
            client_id: 0,
            client_priority: 1,
            target_date: new Date().toISOString().substr(0, 10),
            product_area_id: 0
          });
          $('.modal').modal('hide');
        } else {
          alert('Unexpected server error when creating feature request.');
        }
      });
    };

    self.getClientNameById = (id) => {
      return self.clientMap[id].name;
    };

    self.getProductAreaNameById = (id) => {
      return self.productAreaMap[id].name;
    };
  }
}
