import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "./components"

Page {
    id: root

    property color backgroundColor
    property color buttonLighterColor
    property color buttonDarkerColor
    property color borderColor
    property color fieldColor       
    property color fontColor
    property string fontFamily
    
    visible: true

    //Background
    Rectangle {
        anchors.fill: parent
        color: root.backgroundColor
    }

    //Header
    Rectangle {
        id: header
        
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        height: 50

        color: root.backgroundColor
        
        //Header Title
        Text {
            text: "POLYOU"
            color: root.fontColor
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left

            anchors.leftMargin: 10
            
            font.pixelSize: parent.height * 0.6
            font.family: root.fontFamily
            font.bold: true
        }
    }

    //Header Border
    Rectangle {
        id: headerBorder

        anchors.top: header.bottom
        width: header.width
        height: 1

        color: root.borderColor
    }

    //Footer
    Rectangle {
        id: footer

        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right

        height: 20

        color: root.backgroundColor
    }

    //Footer Border
    Rectangle {
        id: footerBorder

        anchors.bottom: footer.top
        width: footer.width
        height: 1

        color: root.borderColor
    }

    //Workspace
    Rectangle {
        id: workspace

        anchors.top: headerBorder.bottom
        anchors.bottom: footerBorder.top
        anchors.left: sideBar.right
        anchors.right: parent.right

        Loader {
            id: workspaceLoader

            anchors.fill: parent
            sourceComponent: homePage
            
            Component {
                id: homePage

                Page {
                    anchors.fill: workspace

                    Text {
                        anchors.centerIn: parent
                        text: qsTr("HOME PAGE")
                        font.pixelSize: 50
                    }
                    
                }
            }

            Component {
                id: reviewPage

                Page {
                    anchors.fill: workspace

                    Text {
                        anchors.centerIn: parent
                        text: qsTr("REVIEW PAGE")
                        font.pixelSize: 50
                    }
                }
                   
            }
            
            Component {
                id: createPage

                Page {
                    anchors.fill: workspace
                
                    Text {
                        anchors.centerIn: parent
                        text: qsTr("CREATE PAGE")
                        font.pixelSize: 50
                    }   
                }
            }

        }
    }

    SideBar {
        id: sideBar

        anchors.top: headerBorder.bottom
        anchors.bottom: footerBorder.top
        anchors.left: parent.left

        color: root.backgroundColor
        borderColor: root.borderColor

        width: 50

        ColumnLayout {
            width: parent.width
            spacing: 0

            Repeater {
                model: [
                    {"iconURL": "qrc:/images/home_icon.svg", "floatText": qsTr("Home Page"),             "pageID": homePage},
                    {"iconURL": "qrc:/images/book_icon.svg", "floatText": qsTr("Review Flashcards"),     "pageID": reviewPage},
                    {"iconURL": "qrc:/images/plus_icon.svg", "floatText": qsTr("Create New Flashcards"), "pageID": createPage}
                ]

                SideButton {
                    Layout.fillWidth: true
                    
                    iconURL: modelData.iconURL
                    floatText: modelData.floatText
                    pageID: modelData.pageID
                    currentPageID: workspaceLoader.sourceComponent

                    height: sideBar.width

                    backgroundColor: root.backgroundColor
                    selectBorderColor: root.buttonLighterColor
                    bottomBorderColor: root.borderColor

                    onClicked: function(id) {
                        workspaceLoader.sourceComponent = id
                    }
                }
            }
        }
    }
}