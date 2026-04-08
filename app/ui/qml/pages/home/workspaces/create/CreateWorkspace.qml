import QtQuick
import QtQuick.Controls

import "../../../../style"
import "./components/flashcard_input"

Page {
    id: root

    //Background
    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor
    }

    ScrollView {
        anchors.fill: parent

        Column {
            width: root.width

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                
                text: qsTr('CREATE FLASHCARDS')
                font.family: Style.fontFamily
                font.pixelSize: 50
                font.bold: true
                color: Style.fontColor
            }
            
            FlashcardsInput {
                anchors.horizontalCenter: parent.horizontalCenter
            
                width: parent.width
                height: 800
            }
        }
    }
}