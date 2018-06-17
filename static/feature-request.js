'use strict';

/*
class FeatureRequest {
  constructor(id, title, description, client, target_date, product_area) {
    this.id = id;
    this.title = title;
    this.description = description;
    this.client = client;
    this.target_date = target_date;
    this.product_area = product_area;
  }
}
*/

class FeatureRequestModule {

  constructor() {}

  getAll(cb) {
    $.get('/feature_request', (data) => {
      /*
      const frs = [];
      for (const c in data) {
        frs.push(new FeatureRequest(c.id, c.title, c.description, c.client, c.target_date, c.product_area));
      }
      cb(frs);
      */
      cb(data);
    });
  }

  create(fr, cb) {
    $.post('/feature_request', fr, (data) => {
      cb(null, data);
    }).fail(() => {
      const msg = 'Failed to create feature request.';
      console.log(msg);
      cb(msg, null);
    });
  }

  getOne(id, cb) {
    $.get('/feature_request/' + id, (data) => {
        // const fr = new FeatureRequest(data.id, data.title, data.description, data.client, data.target_date, data.product_area);
        // cb(fr);
        cb(data);
    });
  }

  update(fr, cb) {
    $.ajax({
      type: 'PUT',
      url: '/feature_request/' + fr.id,
      data: fr,
      success: (data) => {
        cb(null, data);
      }
    }).fail(() => {
      const msg = 'Failed to update feature request.';
      console.log(msg);
      cb(msg, null);
    });
  }

  remove(id, cb) {
    $.ajax({
      type: 'DELETE',
      url: '/feature_request/' + id,
      data: fr,
      success: (data) => {
        cb(null, data);
      }
    }).fail(() => {
      const msg = 'Failed to delete feature request.';
      console.log(msg);
      cb(msg, null);
    });
  }
}
