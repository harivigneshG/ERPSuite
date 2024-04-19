if(frappe.boot.suite_btn_listview) {
  
  frappe.listview_settings['Sales Order'] = {
      button: {
          show: function(doc) {
          return true;
          },
          get_label: function() {
          return 'Get Info';
          },
          get_description: function(doc) {
          return ("Click to View")
          },
          action: function(doc) {

            //gets sales order's info details
            frappe.db.get_doc('Sales Order', doc.name, ['order_type', 'grand_total']).then(m => {

              frappe.msgprint({
                title: m.name,
                indicator: 'green',
                message: 
                `<table class="table table-bordered">
                <thead>
                  <tr>
                    <th scope="col">Type</th>
                    <th scope="col">Grand Total</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>${m.order_type}</td>
                    <td>${m.grand_total}</td>
                  </tr>
                </tbody>
                </table>`
              });
            })
          
          }
      }
    }
}