import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.gateways.http.auth import AuthGatewayHTTP
from app.core.schemas.auth.requests import TokenRequest

if __name__ == "__main__":    
    http = RequestsHTTPClient(
        base_url= 'http://127.0.0.1:8000/'
    )
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