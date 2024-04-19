import frappe

@frappe.whitelist()
def budget_validate(doc,method=None):
    settings=frappe.get_cached_doc("ERPSuite Settings")
    if settings.max_budget_amount:
        if doc.grand_total >= settings.max_budget_amount:
            frappe.throw(msg="Purchase Order amount exceeds Budget", title=("Budget Limit Exceeds"))


@frappe.whitelist()
def create_drop_ship(doc,method=None):
    validate_supplier_details(doc)
    create_purchase_order(doc)
      

@frappe.whitelist()
def validate_supplier_details(doc):

    settings=frappe.get_cached_doc("ERPSuite Settings")
    if settings.max_budget_amount:
        if doc.grand_total >= settings.max_budget_amount:
            frappe.throw(msg="Purchase Order amount exceeds Budget", title=("Budget Limit Exceeds"))
            
    ''' Validates item's supplier details and checkboxes '''
    if doc.generated_by_erpsuite:
        if len(doc.items) > 0:
            for item in doc.items:
                item.warehouse =""
                if not item.delivered_by_supplier:
                    item.delivered_by_supplier = 1
                if not item.supplier:
                    frappe.throw("Select Item {}'s Supplier to Create Drop Shipping".format(item.item_code))
        else:
            return

@frappe.whitelist()
def create_purchase_order(doc):
    try:
        if doc.generated_by_erpsuite:
            po=frappe.new_doc("Purchase Order")
            po.transaction_date = doc.transaction_date
            po.supplier = doc.generated_by_erpsuite_supplier
            po.company = doc.company
            po.currency = doc.currency
            po.total_qty = doc.total_qty
            po.base_total = doc.base_total
            po.grand_total = doc.grand_total

            for item in doc.items:
                new_row = po.append("items", {})
                new_row.item_code = item.item_code
                new_row.schedule_date = item.delivery_date
                new_row.item_name = item.item_name
                new_row.qty = item.qty
                new_row.uom = item.uom
                new_row.base_rate = item.base_rate
                new_row.base_amount = item.base_amount
                new_row.sales_order = doc.name
                new_row.delivered_by_supplier = 1
                new_row.apply_tds = 1

            po.flags.ignore_mandatory =True
            po.save().submit()
    except Exception as e:
        frappe.throw("error occured " ,str(e))
    finally:
        if po.name:
            frappe.msgprint("Drop Shipping PO Added {} ".format(po.name), alert=True)








                

