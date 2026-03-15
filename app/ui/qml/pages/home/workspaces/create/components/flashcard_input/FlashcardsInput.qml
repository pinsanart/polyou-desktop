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
    }

    Component.onCompleted: {
        webchan.registerObjects({
            "flashcardViewModel": flashcardViewModel,
            "editorState": editorState
        })
        webview.url = Qt.resolvedUrl("./index.html")
    }
}