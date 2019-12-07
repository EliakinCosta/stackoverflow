import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.13

Window {
    visible: true
    width: 640
    height: 480

    Menu {
        id: contextMenu

        MenuItem {
            text: "Object1"
            onTriggered: console.log(text + " selected")
        }

        Button {
            id: fileButton
            text: "Object2"
            onClicked: console.log("eliakin")
            onHoveredChanged: console.log("test")

            Menu {
                id: menu
                y: fileButton.height

                MenuItem {
                    text: "New..."
                }
                MenuItem {
                    text: "Open..."
                }
                MenuItem {
                    text: "Save"
                }
            }
        }
    }

    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.RightButton
        onClicked: {
            if (mouse.button === Qt.RightButton)
                contextMenu.popup()
        }
    }
}
