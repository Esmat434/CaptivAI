# Django Settings
DEBUG=False
SECRET_KEY=your_secret_key_here 

ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8080,http://127.0.0.1:8080

# ===================================================================
# Database INITIALIZATION variables FOR MYSQL CONTAINER (این بخش برای خود کانتینر MySQL است)
# ===================================================================
MYSQL_DATABASE=your_db_name
MYSQL_USER=your_db_user
MYSQL_PASSWORD=your_db_password
MYSQL_ROOT_PASSWORD=your_db_root_password
