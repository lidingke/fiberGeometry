import os

MODBUS_PORT = 'com14'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR' + BASE_DIR)

VIEW_LABEL = False

PDF_PARAMETER = {}
DB_PARAMETER = {}

#todo:error old data save

SAVED_VIEW_ITEMS = {}

DYNAMIC_CAMERA = True

LED_GREEN_CORE_CURRENT = 100
LED_RED_BACKGROUND_CURRENT = 600
