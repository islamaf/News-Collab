# general app config
import os

secret_key = os.urandom(12)  # Secret validation key
users_db_path = 'credentials.db'
posts_db_path = 'interaction.db'
