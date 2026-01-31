import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.flashcards.flashcard_http_gateway import FlashcardsHTTPGateway
from app.dependencies.config.config import settings
from app.dependencies.auth.auth_http_gateway import AuthHTTPGateway

from app.core.schemas.flashcards import FlashcardInfo, FlashcardFSRS, FlashcardImage, FieldsEnum, FlashcardContent, FlashcardAudio, FlashcardReview, RatingEnum, StateEnum
from app.dependencies.time.utc_safe import utcnow

from app.infrastructure.repositories.flashcard_repository_sqlalchemy import FlashcardRepositorySQLAlchemy

if __name__ == "__main__":
    flashcard_repository = FlashcardRepositorySQLAlchemy()
    
    http_client = RequestsHTTPClient(settings.POLYOU_URL)

    access_token = AuthHTTPGateway(http_client).login('test@test.com', 'test')['access_token']

    http_client.token = access_token
    
    flashcard_http_gateway = FlashcardsHTTPGateway(http_client)

    id = flashcard_repository.list_ids()
    
    print(flashcard_repository.get_info(id[0]))

    flashcard_repository.touch(id[0])

    print(flashcard_repository.get_info(id[0]))

    print(flashcard_http_gateway.get_flashcards_ids())
    
    #print(get_flashcard_updated_at(1))
    #print(update_flashcard_fsrs(1, FlashcardFSRS()))
    #print(update_flashcard_images(1, [FlashcardImage(field=FieldsEnum.front, image_url="url")]))
    #print(update_flashcard_content(1, FlashcardContent(front_field="Arthur", back_field="Pinheiro")))
    #print(update_flashcard_audios(1, [FlashcardAudio(field=FieldsEnum.front, audio_url="url")]))
    #print(update_flashcard_reviews(1, [FlashcardReview(reviewd_at=utcnow(), rating=RatingEnum.AGAIN, response_time_ms=1000, scheduled_days=1, actual_days=1, prev_stability=0.1, prev_difficulty=5, new_stability= 2.0, new_difficulty= 4.0, state_before= StateEnum.LEARNING, state_after=StateEnum.REVIEW)]))
    #print(get_flashcard_info(1))
    
'''
    http_client = RequestsHTTPClient(settings.POLYOU_URL)

    auth_gateway = AuthHTTPGateway(http_client)
    
    access_token = auth_gateway.login("test@test.com", "test")['access_token']
    http_client.token = access_token

    flashcard_gateway = FlashcardsHTTPGateway(http_client)

    flashcards_ids = flashcard_gateway.get_flashcards_ids()
    flashcards_info = flashcard_gateway.get_flashcard_info(flashcards_ids)

    print(flashcards_info) 

    flashcard_info = FlashcardInfo(**flashcards_info[0])

    flashcard_info.content.front_field = 'sucess'
    #insert_flashcard(flashcard_info)
    
    print(flashcard_info)


    print(get_flashcard_info(1))    


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