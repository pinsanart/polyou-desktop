import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "../../style/"

import "./components"
import "./workspaces/home"
import "./workspaces/review"
import "./workspaces/create"

Page {
    id: root
    
    visible: true

    //Background
    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor
    }

    //Header
    Rectangle {
        id: header
        
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        height: 50

        color: Style.backgroundColor
        
        //Header Title
        Text {
            text: "POLYOU"
            color: Style.fontColor
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left

            anchors.leftMargin: 10
            
            font.pixelSize: parent.height * 0.6
            font.family: Style.fontFamily
            font.bold: true
        }
    }

    //Header Border
    Rectangle {
        id: headerBorder

        anchors.top: header.bottom
        width: header.width
        height: 1

        color: Style.borderColor
    }

    //Footer
    Rectangle {
        id: footer

        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right

        height: 20

        color: Style.backgroundColor
    }

    //Footer Border
    Rectangle {
        id: footerBorder

        anchors.bottom: footer.top
        width: footer.width
        height: 1

        color: Style.borderColor
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
            sourceComponent: createWorkspace
            
            Component {
                id: homeWorkspace

                HomeWorkspace {
                    anchors.fill: workspace
                }
            }

            Component {
                id: reviewWorkspace

                ReviewWorkspace {
                    anchors.fill: workspace
                }
            }
            
            Component {
                id: createWorkspace
                
                CreateWorkspace {}
            }

        }
    }

    SideBar {
        id: sideBar

        anchors.top: headerBorder.bottom
        anchors.bottom: footerBorder.top
        anchors.left: parent.left

        color: Style.backgroundColor
        borderColor: Style.borderColor

        width: 50

        ColumnLayout {
            width: parent.width
            spacing: 0

            Repeater {
                model: [
                    {"iconURL": "qrc:assets/images/home_icon.svg", "floatText": qsTr("Home Page"),             "workspaceID": homeWorkspace},
                    {"iconURL": "qrc:assets/images/book_icon.svg", "floatText": qsTr("Review Flashcards"),     "workspaceID": reviewWorkspace},
                    {"iconURL": "qrc:assets/images/plus_icon.svg", "floatText": qsTr("Create New Flashcards"), "workspaceID": createWorkspace}
                ]

                SideButton {
                    Layout.fillWidth: true
                    
                    iconURL: modelData.iconURL
                    floatText: modelData.floatText
                    workspaceID: modelData.workspaceID
                    currentWorkspaceID: workspaceLoader.sourceComponent

                    height: sideBar.width

                    onClicked: function(id) {
                        workspaceLoader.sourceComponent = id
                    }
                }
            }
        }
    }
}