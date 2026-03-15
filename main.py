import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTranslator

import resources_rc

from uuid import uuid4

import app.dependencies.sqlalchemy.registrations.mappers 
import app.dependencies.sqlalchemy.registrations.repositories
import app.dependencies.sqlalchemy.registrations.services

from app.core.bootstrap import Bootstrap

from app.core.config.http import http_settings
from app.core.config.paths import path_settings
from app.core.config.db import db_settings
from app.core.config.app import app_settings
from app.core.config.desktop import desktop_settings


from app.dependencies.sqlalchemy.db.factory import DBConnectionFactory

from app.ui.viewmodels.auth import AuthViewModel

from app.services.managers.auth_session import AuthSessionManager
from app.services.managers.editor_state import EditorStateManager

from app.dependencies.gateways.http.auth import AuthGatewayHTTP
from app.dependencies.http.authenticated_client import AuthenticatedHTTPClient
from app.dependencies.http.requests_client import RequestsHTTPClient
from app.dependencies.storage.local import LocalStorage

from app.core.security.access_token_provider import AccessTokenProvider
from app.core.security.refresh_token_vault import RefreshTokenVault

from app.ui.viewmodels.flashcards import FlashcardViewModel
from app.ui.states.editor import EditorState

if __name__ == "__main__":
    db_connection = DBConnectionFactory.create(
        DATABASE_URL= db_settings.DATABASE_URL,
        DEBUG= app_settings.DEBUG
    )

    bootstrap = Bootstrap(
        db_connection= db_connection,
        app_path= path_settings.APP_PATH,
        db_file_path= path_settings.DATABASE_FILE_PATH
    )

    bootstrap.run()

    access_token_provider = AccessTokenProvider()
    refresh_token_vault = RefreshTokenVault(
        service_name=app_settings.APP_NAME
    )

    raw_http = RequestsHTTPClient(
        base_url= http_settings.BASE_URL
    )

    authenticated_http = AuthenticatedHTTPClient(
        http_client= raw_http,
        access_token_provider= access_token_provider
    )

    auth_gateway = AuthGatewayHTTP(
        authenticated_http_client= authenticated_http
    )

    auth_manager = AuthSessionManager(
        auth_gateway= auth_gateway,
        access_token_provider= access_token_provider,
        refresh_token_vault= refresh_token_vault
    )


    auth_vm = AuthViewModel(
        auth_manager= auth_manager,
        device_id= uuid4(),
        device_name= desktop_settings.DESKTOP_NAME,
        username= desktop_settings.USERNAME
    )

    ui_app = QApplication(sys.argv)
    ui_engine = QQmlApplicationEngine()

    translator = QTranslator()
    translator.load("app/translations/en.qm")    
    ui_app.installTranslator(translator)

    qmlRoot = Path(__file__).resolve().parent / 'app' / 'ui' / 'qml'
    
    ui_engine.addImportPath(qmlRoot)
    
    #VIEWMODELS
    flashcard_viewmodel = FlashcardViewModel()
    
    #STATES
    editor_state = EditorState(
        editor_state_manager= EditorStateManager(
            local_storage= LocalStorage(path_settings.STATES_PATH),
            filename= 'editor.json'
        )
    )

    #SET VIEWMODELS AND STATES
    ui_engine.rootContext().setContextProperty("app_name", app_settings.APP_NAME)
    ui_engine.rootContext().setContextProperty("flashcardViewModel", flashcard_viewmodel)
    ui_engine.rootContext().setContextProperty("editorState", editor_state)

    #LOAD
    ui_engine.load(str(qmlRoot / 'MainWindow.qml'))

    if not ui_engine.rootObjects():
        print("'MainWindow.qml' was not found.")
        sys.exit(-1)
    
    sys.exit(ui_app.exec())