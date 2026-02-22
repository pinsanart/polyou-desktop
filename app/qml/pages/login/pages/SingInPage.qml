import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: root

    property color backgroundColor
    property color buttonLighterColor
    property color buttonDarkerColor
    property color borderColor
    property color fieldColor       
    property color fontColor
    property string fontFamily
    
    signal openSingUpPage() 

    //BACKGROUND
    Rectangle {
        anchors.fill: parent
        color: root.backgroundColor
    }



    ColumnLayout {
        anchors.centerIn: parent
        
        spacing: 10
        //Title
        Text {
            Layout.alignment:       Qt.AlignCenter

            text: "LOGIN"
            color: root.fontColor

            font.bold: true
            font.family: root.fontFamily
            font.pixelSize: parent.height * 0.3
        }

        //Email Field
        Rectangle {
            Layout.alignment:       Qt.AlignCenter
            Layout.preferredWidth:  root.width * 0.6
            Layout.preferredHeight: root.height * 0.05

            color: root.fieldColor

            TextField {
                id: email_field

                anchors.fill: parent
                color: root.fontColor
                font.pixelSize: parent.height * 0.6
                placeholderText: "Email"

                background: Rectangle {
                    anchors.fill: parent
                    color: root.fieldColor
                }
            }
        }

        //Password Field
        Rectangle {
            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: root.width * 0.6
            Layout.preferredHeight: root.height * 0.05
            
            color: root.fieldColor

            TextField {
                id: password_field

                anchors.fill: parent
                color: root.fontColor
                font.pixelSize: parent.height * 0.6
                echoMode: TextInput.Password
                passwordMaskDelay: 250
                placeholderText: "Password"

                background: Rectangle {
                    anchors.fill: parent
                    color: root.fieldColor
                }
            }
        }

        //Sing In Button
        Button {
            id: singInButton

            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: root.width * 0.2
            Layout.preferredHeight: root.height * 0.04

            background: Rectangle {
                anchors.fill: parent
                color: root.buttonLighterColor 

                Text {
                    anchors.centerIn: parent
                    text: "Sing In"
                    font.family: root.fontFamily
                    font.pixelSize: parent.height * 0.6
                    color: root.fontColor
                }
            }

            onClicked: {
                
            }

        }

        // "OR" line
        RowLayout {
            Layout.alignment: Qt.AlignCenter
            spacing: 6

            Rectangle {
                Layout.preferredWidth: root.width * 0.3
                height: 2

                color: root.borderColor
            }

            Text {
                text: "or"
                color: root.borderColor

                font.pixelSize: 20
                font.family: root.fontFamily
            }
            
            Rectangle {
                Layout.preferredWidth: root.width * 0.3
                height: 2

                color: root.borderColor
            }
        }

        //Sing Up Button
        Button {
            id: singUpButton

            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: root.width * 0.2
            Layout.preferredHeight: root.height * 0.04

            background: Rectangle {
                anchors.fill: parent
                color: root.buttonDarkerColor 

                Text {
                    text: "Sing Up"

                    anchors.centerIn: parent
                    font.pixelSize: parent.height * 0.6
                    font.family: root.fontFamily
                    color: root.fontColor
                }
            }

            onClicked: {
                root.openSingUpPage()
            }           
        }
    }
}