import QtQuick

Rectangle {
    id: root

    property string iconURL
    property string floatText
    
    property var workspaceID
    property var currentWorkspaceID

    property color backgroundColor
    property color selectBorderColor
    property color bottomBorderColor

    signal clicked(var workspaceID)

    width: parent.width
    color: root.backgroundColor

    // Select Border
    Rectangle {
        id: selectBorder

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        width: 2
        visible: root.currentWorkspaceID === root.workspaceID
        color: root.selectBorderColor
    }

    // Bottom Border
    Rectangle {
        id: bottomBorder

        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right

        height: 1
        color: root.bottomBorderColor
    }

    //Icon
    Image {
        id: icon

        anchors.centerIn: parent

        source: root.iconURL
        width: parent.width * 0.6
        height: parent.height * 0.6
        sourceSize.width: width
        sourceSize.height: height
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true

        onClicked: {
            root.clicked(root.workspaceID)
        }
    }
}