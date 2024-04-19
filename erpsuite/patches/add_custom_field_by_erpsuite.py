from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    create_custom_field(
        "Sales Order",
        {
            "default": "0",
            "fieldname": "generated_by_erpsuite",
            "fieldtype": "Check",
            "label": "Create Drop Shipping Purchase Order",
            "insert_after": "delivery_date"
        }
    )