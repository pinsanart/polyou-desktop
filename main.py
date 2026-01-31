
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.flashcards.flashcard_http_gateway import FlashcardsHTTPGateway
from app.dependencies.config.config import settings
from app.dependencies.auth.auth_http_gateway import AuthHTTPGateway

from app.crud.flashcards import get_flashcards_ids, insert_flashcard
from app.core.shemas.flashcards import FlashcardInfo
from app.db.migrations import drop_all, create_all

if __name__ == "__main__":
    http_client = RequestsHTTPClient(settings.POLYOU_URL)

    auth_gateway = AuthHTTPGateway(http_client)
    
    access_token = auth_gateway.login("test@test.com", "test")['access_token']
    http_client.token = access_token

    flashcard_gateway = FlashcardsHTTPGateway(http_client)

    flashcards_ids = flashcard_gateway.get_flashcards_ids()
    flashcards_info = flashcard_gateway.get_flashcard_info(flashcards_ids)

    print(flashcards_info) 

    flashcard_info = FlashcardInfo(**flashcards_info[0])

    insert_flashcard(flashcard_info)

    print(get_flashcards_ids())    


    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRoot = Path(__file__).resolve().parent / 'app' / 'qml'
    
    engine.addImportPath(qmlRoot)
   
    engine.load(str(qmlRoot / 'MainWindow.qml'))

    if not engine.rootObjects():
        print("'MainWindow.qml' was not found.")
        sys.exit(-1)
    
    sys.exit(app.exec())
