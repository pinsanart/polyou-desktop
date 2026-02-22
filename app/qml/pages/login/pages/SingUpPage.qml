import QtQuick
import QtQuick.Controls

Page {
    property color backgroundColor
    property color buttonLighterColor
    property color buttonDarkerColor
    property color borderColor
    property color fieldColor       
    property color fontColor
    property string fontFamily
    
    //BACKGROUND
    Rectangle {
        anchors.fill: parent
        color: "red"
    }
}