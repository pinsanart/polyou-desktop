import QtQuick
import QtQuick.Controls

import "./pages/"

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
    
    property color backgroundColor:     '#292b31'
    property color buttonLighterColor:  "#187DF0"
    property color buttonDarkerColor:   "#0C3F78"
    property color borderColor:         "#4A4F5A"
    property color fieldColor:          "#4A4F5A"
    property color fontColor:           "#F5F5F5"
    property string fontFamily:         "Roboto"

    Loader {
        id: pageLoader
        anchors.fill: parent

        sourceComponent: homePage
        Component {
            id: homePage    
            HomePage {
                backgroundColor:     root.backgroundColor
                buttonLighterColor:  root.buttonLighterColor
                buttonDarkerColor:   root.buttonDarkerColor
                borderColor:         root.borderColor
                fieldColor:          root.fieldColor
                fontColor:           root.fontColor
                fontFamily:          root.fontFamily
            }
        }
    }
}