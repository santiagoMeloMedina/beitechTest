
from flask_swagger_ui import get_swaggerui_blueprint
from constant.values import APP_NAME

route = get_swaggerui_blueprint("/docs", "/swagger.json", config={
    'app_name': APP_NAME
})