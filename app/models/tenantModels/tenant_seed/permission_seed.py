role_permissions_map = {
  "super_admin": [
    "read_all_employee",
    "create_employee",
    "update_employee",
    "delete_employee",

    "read_all_offices",
    "create_office",
    "update_office",
    "delete_office",

    "read_all_customers",
    "create_customer",
    "update_customer",
    "delete_customer",

    "read_all_pickups",
    "create_pickups",
    "update_pickups",
    "delete_pickups",


    "read_all_dockets",
    "create_docket",
    "update_docket",
    "delete_docket",

    "read_all_manifests",
    "create_manifest",
    "update_manifest",
    "delete_manifest",

    "read",
    "update",
    "delete",
    "assign_role",
    "assign_permission",
  ],
  "admin": ["create_pickup","read", "update", "delete", "assign_role", "assign_permission"],
  "office_staff": [
    "create_pickup",
    "read",
    "update",
    "delete",
    "assign_role",
    "assign_permission",
  ],
  "driver": ["read", "update", "delete", "assign_role", "assign_permission"],
}
