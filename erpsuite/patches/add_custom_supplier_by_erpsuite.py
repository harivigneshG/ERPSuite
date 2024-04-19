from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    create_custom_field(
        "Sales Order",
        {
            "fieldname": "generated_by_erpsuite_supplier",
            "fieldtype": "Link",
            "options": "Supplier",
            "label": "Supplier",
            "insert_after": "generated_by_erpsuite",
            "mandatory_depends_on": "eval:doc.generated_by_erpsuite==1",
            "depends_on": "eval:doc.generated_by_erpsuite==1"
        }
    )