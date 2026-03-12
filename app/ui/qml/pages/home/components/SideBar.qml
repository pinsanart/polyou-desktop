import QtQuick

Rectangle {
    id: root

    property color borderColor
    default property alias content: container.children

    //Lateral Border
    Rectangle {
        id: border

        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: parent.right

        width: 1

        color: root.borderColor
    }

    Item {
        id: container
        anchors.fill: parent
    }
}