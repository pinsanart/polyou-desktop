import QtQuick
import QtQuick.Controls

import "./pages/login"

//MAIN WINDOW
Window {
    id: root
    
    width: Screen.width
    height: Screen.height

    minimumWidth:  1280
    minimumHeight: 720

    visible: true
    title: "POLYOU"
    flags: Qt.WindowTitleHint
    
    property color backgroundColor:     "#353840"
    property color buttonLighterColor:  "#187DF0"
    property color buttonDarkerColor:   "#0C3F78"
    property color borderColor:         "#4A4F5A"
    property color fieldColor:          "#4A4F5A"
    property color fontColor:           "#F5F5F5"
    property string fontFamily:         "Roboto"


    Loader {
        id: pageLoader
        anchors.fill: parent

        sourceComponent: loginPage

        Component {
            id: loginPage    

            LoginPage {
                backgroundColor:    root.backgroundColor
                buttonLighterColor: root.buttonLighterColor
                buttonDarkerColor:  root.buttonDarkerColor
                borderColor:        root.borderColor
                fieldColor:         root.fieldColor
                fontColor:          root.fontColor
                fontFamily:         root.fontFamily
            }
        }
    }
}