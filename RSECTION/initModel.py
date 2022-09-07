import sys
import RSECTION.dependencies
import requests
from suds.client import Client
from RSECTION.enums import ObjectTypes, ModelType, AddOn
from RSECTION.suds_requests import RequestsTransport

# Connect to server
# Check server port range set in "Program Options & Settings"
# By default range is set between 8101 ... 8109
print('Connecting to server...')
try:
    client = Client('http://localhost:8101/wsdl')
except:
    print('Error: Connection to server failed!')
    print('Please check:')
    print('- If you have started RFEM application')
    print('- If all RSECTION dialogs are closed')
    print('- If server port range is set correctly')
    print('- If you have a valid Web Services license')
    print('- Check Program Options & Settings > Web Services')
    sys.exit()

try:
    modelLst = client.service.get_model_list()
except:
    print('Error: Please check if all RSECTION dialogs are closed.')
    input('Press Enter to exit...')
    sys.exit()

# Persistent connection
# Next 4 lines enables Client to work within 1 session which is much faster to execute.
# Without it the session lasts only one request which results in poor performance.
# Assigning session to application Client (here client) instead of model Client
# results also in poor performace.
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1)
session.mount('http://', adapter)
trans = RequestsTransport(session)