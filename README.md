
### Beitech Practice Test
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
>   DB_HOST  
    DB_PORT  
    DB_USER  
    DB_NAME  
    DB_PASSWORD  
    DB_SSL_DISABLE  

Tho default values are already set for Beitech testing database