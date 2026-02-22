import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "./pages/"

Page {
    id: root
    visible: true

    property color buttonLighterColor
    property color backgroundColor
    property color buttonDarkerColor
    property color borderColor
    property color fieldColor       
    property color fontColor
    property string fontFamily

    //Background
    Rectangle {
        anchors.fill: parent
        color: root.backgroundColor
    }
    
    //Title
    Item {
        id: titleField
        
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        width: parent.width * 0.45
        
        visible: true

        Column {
            anchors.centerIn: parent
            spacing: 0
            
            Text {
                text: "Welcome to"

                anchors.horizontalCenter: parent.horizontalCenter
                
                color: root.fontColor
                font.pixelSize: root.height * 0.04
                font.family: root.fontFamily
            }

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "POLYOU"
                font.pixelSize: root.height * 0.15
                color: root.fontColor
                font.bold: true
                font.family: root.fontFamily
                padding: 0
            }

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Your jouney to fluency starts here"
                font.pixelSize: root.height * 0.04
                color: root.fontColor
                font.family: root.fontFamily
                padding: 0
            }
        }
    }

    //Border
    Rectangle {
        width: 2
        height: 0.9 * parent.height
        
        anchors.right: titleField.right
        anchors.verticalCenter: parent.verticalCenter

        color: root.borderColor
    }

    Item {
        id: loaderField
        
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        width: parent.width * 0.55

        Loader {
            id: pageLoader
            
            anchors.fill: parent
            
            sourceComponent: singInPage

            Component {
                id: singInPage

                SingInPage {
                    backgroundColor:    root.backgroundColor
                    buttonLighterColor: root.buttonLighterColor
                    buttonDarkerColor:  root.buttonDarkerColor
                    borderColor:        root.borderColor
                    fieldColor:         root.fieldColor
                    fontColor:          root.fontColor
                    fontFamily:         root.fontFamily

                    onOpenSingUpPage: {
                        pageLoader.sourceComponent = singUpPage
                    }
                }
            }
            
            Component {
                id: singUpPage

                SingUpPage {
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
}