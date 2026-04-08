import QtQuick
import QtWebEngine
import QtWebChannel  

Rectangle {
    WebChannel {
        id: webchan
    }

    WebEngineView {
        id: webview

        anchors.fill: parent

        objectName: "webview"
        webChannel: webchan

        onJavaScriptConsoleMessage: function(level, message, lineNumber, sourceID) {
            console.log(`[JS ${level}] ${message} (${sourceID}:${lineNumber})`)
        }
    }

    Component.onCompleted: {
        webchan.registerObjects({
            "flashcardBridge": flashcardBridge,
            "editorStateBridge": editorStateBridge,
            "mediaBridge": mediaBridge
        })
        webview.url = Qt.resolvedUrl("./index.html")
    }
}