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

class Model():
    clientModel = None
    clientModelLst = []
    activeSession = False

    def __init__(self,
                 new_model: bool=True,
                 model_name: str="TestModel",
                 delete: bool=False,
                 delete_all: bool=False):
        """
        Class object representing individual model in RFEM.
        Class enables to edit multiple models in one session through holding
        one transport session active by not setting 'trans' into Client.
        Args:
            new_model (bool, optional): Set to True if new model is requested.
            model_name (str, optional): Defaults to "TestModel".
            delete (bool, optional):  Delete results
            delete_all (bool, optional): Delete all objects in Model.
        """

        cModel = None
        modelLs = client.service.get_model_list()

        if new_model:
            if modelLs and model_name in modelLs.name:
                modelIndex = 0
                for i,j in enumerate(modelLs.name):
                    if modelLs.name[i] == model_name:
                        modelIndex = i
                new = client.service.get_model(modelIndex) + 'wsdl'
                # Set transport parameter if it is the first model
                if Model.activeSession:
                    cModel = Client(new)
                else:
                    cModel = Client(new, transport=trans)
                cModel.service.delete_all_results()
                cModel.service.delete_all()
            else:
                new = client.service.new_model(model_name) + 'wsdl'
                if Model.activeSession:
                    cModel = Client(new)
                else:
                    cModel = Client(new, transport=trans)
                if not modelLs:
                    Model.activeSession = True
        else:
            modelIndex = 0
            for i,j in enumerate(modelLs.name):
                if modelLs.name[i] == model_name:
                    modelIndex = i
            new = client.service.get_model(modelIndex) + 'wsdl'
            if Model.activeSession:
                cModel = Client(new)
            else:
                cModel = Client(new, transport=trans)
            if delete:
                print('Deleting results...')
                cModel.service.delete_all_results()
            if delete_all:
                print('Delete all...')
                cModel.service.delete_all()

        # when using multiple intances/model
        self.clientModel = cModel
        if not modelLs or not model_name in modelLs.name:
            Model.clientModelLst.append(cModel)
        # when using only one instace/model
        Model.clientModel = cModel

