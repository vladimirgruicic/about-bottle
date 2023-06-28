from models import User

User.create_table_users()

User.create_table_about()

User.create_table_contacts()

User.create_table_zlatan()

User.insert_user('vlado', 'vlado@mail.com')

User.get_all_users()