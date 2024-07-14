import sys
from os import path

sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '..')))

from pymalex import PyMalex, MalexUsers

def main():
    pymalex_instance = PyMalex("http://localhost:5000", "key", debug=True)
    
    users_handler = MalexUsers(pymalex_instance)

    print("Liste des utilisateurs:")
    users_list = users_handler.list_users()
    print(users_list)

    new_user_data = {
        "username": "John Doe",
        "mail": "john.doe@example.com",
        "group": "User"
    }
    print("\nAjout d'un nouvel utilisateur:")
    new_user = users_handler.add_user(new_user_data)
    print(new_user)

    user_id_to_modify = "4"
    updated_user_data = {
        "username": "Updated Name",
        "mail": "updated.email@example.com"
    }
    print("\nModification d'un utilisateur:")
    modified_user = users_handler.modify_user(user_id_to_modify, updated_user_data)
    print(modified_user)

    user_id_to_delete = "5"
    print("\nSuppression d'un utilisateur:")
    deleted_user = users_handler.delete_user(user_id_to_delete)
    print(deleted_user)

    user_id_to_view = "3"
    print("\nVisualisation d'un utilisateur:")
    viewed_user = users_handler.get_user(user_id_to_view)
    print(viewed_user)

if __name__ == "__main__":
    main()
