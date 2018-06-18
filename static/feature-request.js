'use strict';

class FeatureRequestModule {

  constructor() {}

  getAll(cb) {
    $.get('/feature_request', (data) => {
      cb(data);
    });
  }

  create(fr, cb) {
    /*
    $.post('/feature_request', fr, (data) => {
      cb(null, data);
    }).fail(() => {
      const msg = 'Failed to create feature request.';
      console.log(msg);
      cb(msg, null);
    });
    */

    $.ajax({
      type: 'POST',
      url: '/feature_request',
      data: JSON.stringify(fr),
      headers: {
        'Content-Type': 'application/json'
      },
      success: (data) => {
        cb(null, data);
      }
    }).fail(() => {
      const msg = 'Failed to create feature request.';
      console.log(msg);
      cb(msg, null);
    });
  }

  getOne(id, cb) {
    $.get('/feature_request/' + id, (data) => {
        cb(data);
    });
  }

  update(fr, cb) {
    $.ajax({
      type: 'PUT',
      url: '/feature_request/' + fr.id,
      data: JSON.stringify(fr),
      headers: {
        'Content-Type': 'application/json'
      },
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
