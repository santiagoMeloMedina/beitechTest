
import os

env = os.environ

PORT = env.get("PORT") if env.get("PORT") else "5000"
DB_HOST = env.get("DB_HOST") if env.get("DB_HOST") else "172.17.0.2"
DB_PORT = env.get("DB_PORT") if env.get("DB_PORT") else "3306"
DB_USER = env.get("DB_USER") if env.get("DB_USER") else "root"
DB_NAME = env.get("DB_NAME") if env.get("DB_NAME") else "Test"
DB_PASSWORD = env.get("DB_PASSWORD") if env.get("DB_PASSWORD") else "123"
DB_SSL_DISABLE = eval(env.get("DB_SSL_DISABLE")) if env.get("DB_SSL_DISABLE") else False