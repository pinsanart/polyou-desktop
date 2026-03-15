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
            "flashcardViewModel": flashcardViewModel,
            "editorState": editorState,
            "mediaViewModel": mediaViewModel
        })
        webview.url = Qt.resolvedUrl("./index.html")
    }
}