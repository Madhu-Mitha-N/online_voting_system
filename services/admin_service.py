from models.admin_model import (
    create_admin,
    get_all_admins,
    get_admin_by_id,
    update_admin,
    delete_admin,
    admin_login
)


def add_admin_service(admin_name, password):
    create_admin(admin_name, password)


def get_admins_service():
    return get_all_admins()


def get_single_admin_service(admin_id):
    return get_admin_by_id(admin_id)


def update_admin_service(admin_id, admin_name, password):
    update_admin(admin_id, admin_name, password)


def delete_admin_service(admin_id):
    delete_admin(admin_id)


def admin_login_service(admin_name, password):
    return admin_login(admin_name, password)