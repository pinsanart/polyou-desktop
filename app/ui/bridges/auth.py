from PySide6.QtCore import QObject, Signal, Property, Slot
from uuid import UUID

from app.services.managers.auth_session import AuthSessionManager
from app.core.schemas.auth.requests import TokenRequest, RefreshRequest, LogoutRequest

class AuthBridge(QObject):
    authStateChanged = Signal()
    loadingChanged = Signal(bool)
    errorOccurred = Signal(str)

    def __init__(self, auth_manager: AuthSessionManager, device_id: UUID, device_name: str, username: str):
        super().__init__()
        self._auth_manager = auth_manager
        self._device_id = device_id
        self._device_name = device_name
        self._username = username

        self._loading = False
        self._is_authenticated = False
        self._current_user = None

    def _set_loading(self, value: bool):
        if self._loading != value:
            self._loading = value
            self.loadingChanged.emit(value)
    
    def get_loading(self):
        return self._loading
    
    def get_is_authenticated(self):
        return self._is_authenticated

    def get_current_user(self):
        return self._current_user
    
    loading = Property(bool, get_loading, notify=loadingChanged)
    isAuthenticated = Property(bool, get_is_authenticated, notify=authStateChanged)
    currentUser = Property(str, get_current_user, notify=authStateChanged)

    @Slot(str, str)
    def login(self, email: str, password: str):
        try:
            self._set_loading(True)

            request = TokenRequest(
                username=       email,
                password=       password,
                device_id=      self._device_id,
                device_name=    self._device_name
            )

            self._auth_manager.login(
                request, 
                self._username
            )

            self._is_authenticated = True
            self._current_user = email
            self.authStateChanged.emit()
        
        except Exception as e:
            self.errorOccurred.emit(str(e))

        finally:
            self._set_loading(False)