import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.gateways.flashcard_http import FlashcardsHTTPGateway
from app.dependencies.config.config import settings
from app.dependencies.gateways.auth_http import AuthHTTPGateway

from app.infrastructure.db.migrations import create_all, drop_all
from app.services.flashcard import FlashcardServiceSQLAlchemy

from app.infrastructure.repositories.flashcards_sqlalchemy import FlashcardRepositorySQLAlchemy
from app.services.flashcard import FlashcardServiceSQLAlchemy
from app.services.language import LanguageServiceSQLAlchemy
from app.infrastructure.repositories.languages_sqlalchemy import LanguageRepositorySQLAlchemy
from app.infrastructure.repositories.flashcard_types_sqlalchemy import FlashcardTypesRepositorySQLAlchemy
from app.services.flashcard_types import FlashcardTypesServiceSQLAlchemy
from app.infrastructure.db.session import SessionLocal

from app.core.schemas.flashcards import FlashcardLocalCreateInfo

from app.infrastructure.repositories.flashcard_local_information import FlashcardLocalInformationRepositorySQLAlchemy
from app.services.flashcards_sync import FlashcardSyncServiceSQLAlchemyHTTP
from app.services.flashcard_local_information import FlashcardLocalInformationServiceSQLAlchemy

from app.dependencies.gateways.flashcard_http import FlashcardsHTTPGateway
from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.gateways.auth_http import AuthHTTPGateway

if __name__ == "__main__":            
    flashcard = {
        "language_iso_639_1": "en",
        "flashcard_type_name": "vocabulary",
        "content": {
            "front_field": "O que é uma closure?",
            "back_field": "Uma função que captura o escopo onde foi criada."
        },
        "images": [
            {
            "field": "front",
            "image_url": "https://cdn.example.com/images/closure-diagram.png"
            }
        ],
        "audios": [
            {
            "field": "back",
            "audio_url": "https://cdn.example.com/audios/closure-explanation.mp3"
            }
        ]
    }

    http_client = RequestsHTTPClient(settings.POLYOU_URL)
    auth_gateway = AuthHTTPGateway(http_client)
    access_token = auth_gateway.login('test@test.com', 'test')['access_token']
    http_client.token = access_token

    flashcard_gateway = FlashcardsHTTPGateway(http_client)

    flashcard_repository = FlashcardRepositorySQLAlchemy(SessionLocal)

    language_repository = LanguageRepositorySQLAlchemy(SessionLocal)
    flashcard_types_repository = FlashcardTypesRepositorySQLAlchemy(SessionLocal)
    language_service = LanguageServiceSQLAlchemy(language_repository)
    flashcard_types_service = FlashcardTypesServiceSQLAlchemy(flashcard_types_repository)

    flashcard_service = FlashcardServiceSQLAlchemy(flashcard_repository, language_service, flashcard_types_service)
    flashcard_local_information_repository = FlashcardLocalInformationRepositorySQLAlchemy(SessionLocal)
    flashcard_local_information_service = FlashcardLocalInformationServiceSQLAlchemy(flashcard_local_information_repository)

    #flashcard_service.create_one(FlashcardLocalCreateInfo(**flashcard))
    flashcard_sync = FlashcardSyncServiceSQLAlchemyHTTP(flashcard_service, flashcard_local_information_service, flashcard_gateway)
    
    #flashcard_sync.sync()

    '''
    print(flashcard_gateway.list_public_ids())
    
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