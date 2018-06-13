let clients = [];
let productAreas = [];

$(document).ready(function() {
  const clientModule = new ClientModule();
  clientModule.getAll((data) => {
    clients = data;
  });

  const productAreaModule = new ProductAreaModule();
  productAreaModule.getAll((data) => {
    productAreas = data;
  });
});
