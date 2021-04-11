
## Beitech Practice Test
Here's the solution API for the `customer_product_order` database. This service was created with **Python3.8**, **Flask** framework and **mysql-connector-python** mysql client library.

#### Installing dependencies
This project is using poetry to help install it's packages, you may also check them out on file `pyproject.toml` to install them with _pip3_. In order to execute poetry virtual environment you can use:
```
    poetry shell
```

Then to install
```
    poetry install
```

#### Running the application
To run the application you must go on the `src` folder and run the file `main.py`. To use a custom database configuration you can set the environmental variables:
>   PORT &rarr; _app port_
    DB_HOST &rarr; _database host ip_  
    DB_PORT &rarr; _database host port_  
    DB_USER &rarr; _database user_  
    DB_NAME &rarr; _database name_  
    DB_PASSWORD &rarr; _database user's password_  
    DB_SSL_DISABLE &rarr; _<**True**|**False**>_  

Default values are currently set for app port `5000` and db host `localhost:3306`, user `root`, password `123`, database `Test`.
