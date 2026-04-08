import QtQuick
import QtQuick.Controls

import "./pages/home"

//MAIN WINDOW
Window {
    id: root
    
    width: Screen.width
    height: Screen.height

    minimumWidth:  1280
    minimumHeight: 720

    flags: Qt.WindowTitleHint
    visible: true
    title: app_name
    
    Loader {
        id: pageLoader
        anchors.fill: parent

        sourceComponent: homePage
        Component {
            id: homePage    
            HomePage {}
        }
    }
}