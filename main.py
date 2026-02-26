import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

import app.dependencies.sqlalchemy.registrations.mappers 
import app.dependencies.sqlalchemy.registrations.repositories
import app.dependencies.sqlalchemy.registrations.services

from app.core.bootstrap import Bootstrap
from app.core.config.paths import path_settings
from app.core.config.db import db_settings
from app.core.config.app import app_settings


from app.dependencies.sqlalchemy.db.factory import DBConnectionFactory


if __name__ == "__main__":
    db_connection = DBConnectionFactory.create(
        DATABASE_URL= db_settings.DATABASE_URL,
        DEBUG= app_settings.DEBUG
    )

    bootstrap = Bootstrap(
        db_connection= db_connection,
        app_path= path_settings.APP_PATH,
        db_path= path_settings.DATABASE_PATH
    )

    bootstrap.run()

    '''
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRoot = Path(__file__).resolve().parent / 'app' / 'ui' / 'qml'
    
    engine.addImportPath(qmlRoot)
   
    engine.load(str(qmlRoot / 'MainWindow.qml'))

    if not engine.rootObjects():
        print("'MainWindow.qml' was not found.")
        sys.exit(-1)
    
    sys.exit(app.exec())
    '''