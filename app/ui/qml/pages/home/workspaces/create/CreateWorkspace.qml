import QtQuick
import QtQuick.Controls

import "./components/flashcard_input"

Page {
    id: root

    property color backgroundColor
    property color buttonLighterColor
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

    ScrollView {
        anchors.fill: parent

        Column {
            width: root.width

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                
                text: qsTr('CREATE FLASHCARDS')
                font.family: root.fontFamily
                font.pixelSize: 50
                font.bold: true
                color: root.fontColor
            }
            
            FlashcardsInput {
                anchors.horizontalCenter: parent.horizontalCenter
            
                width: 800
                height: 800

            }

        }
        
        
    }
}