import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.gateways.http.auth import AuthGatewayHTTP
from app.core.schemas.auth.requests import TokenRequest, RefreshRequest

from app.core.config import settings
from uuid import uuid4
from app.services.refresh_token_vault import RefreshTokenVault

if __name__ == "__main__":
    http = RequestsHTTPClient(settings.BASE_URL)    
    auth_gateway = AuthGatewayHTTP(http)
    vault = RefreshTokenVault(settings.APP_NAME)
    
    '''
    token_request = auth_gateway.token(
        TokenRequest(
            email= 'test@test.com',
            password= 'test',
            device_id= uuid4(),
            device_name= settings.DEVICE_NAME
        )
    )
    '''

    access_token = auth_gateway.refresh(
        RefreshRequest(
            refresh_token= vault.get(settings.USERNAME)
        )
    )

    print(access_token.access_token)

'''
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRoot = Path(__file__).resolve().parent / 'app' / 'qml'
    
    engine.addImportPath(qmlRoot)
   
    engine.load(str(qmlRoot / 'MainWindow.qml'))

    if not engine.rootObjects():
        print("'MainWindow.qml' was not found.")
        sys.exit(-1)
    
    sys.exit(app.exec())
'''