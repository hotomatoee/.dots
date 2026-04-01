import Quickshell
import Quickshell.Wayland
import QtQuick
import QtQuick.Layouts
import Quickshell.Hyprland

PanelWindow {
    id: bar
    anchors.top: true
    anchors.left: true
    anchors.right: true
    implicitHeight: 23
    color: "#cc000000"

    // ── Left: Workspaces ─────────────────────────────────────────────
    RowLayout {
        anchors.left: parent.left
        anchors.verticalCenter: parent.verticalCenter
        anchors.leftMargin: 12
        spacing: 10

        Repeater {
            model: 10
            delegate: Item {
                width: 18
                height: bar.implicitHeight

                property var ws: Hyprland.workspaces.values.find(w => w.id === index + 1)
                property bool isActive: Hyprland.focusedWorkspace?.id === (index + 1)
                property bool isOccupied: ws !== undefined

                Text {
                    anchors.centerIn: parent
                    text: index < 9 ? String(index + 1) : "0"
                    font.family: "Ubuntu Mono Nerd Font"
                    font.pixelSize: 13
                    font.bold: parent.isActive
                    color: parent.isActive   ? "#e0e0e0"
                         : parent.isOccupied ? "#6a6a6a"
                         : "#333333"
                }

                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    onClicked: Hyprland.dispatch("workspace " + (index + 1))
                }
            }
        }
    }

    // ── Centre: Clock ─────────────────────────────────────────────────
    Text {
        id: clock
        anchors.centerIn: parent
        text: Qt.formatDateTime(new Date(), "HH:mm")
        font.family: "Ubuntu Mono Nerd Font"
        font.pixelSize: 13
        font.bold: true
        color: "#d0d0d0"

        Timer {
            interval: 1000
            running: true
            repeat: true
            onTriggered: clock.text = Qt.formatDateTime(new Date(), "HH:mm")
        }
    }

    // ── Right: Label ──────────────────────────────────────────────────
    Text {
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter
        anchors.rightMargin: 12
        text: "Donda"
        font.family: "Ubuntu Mono Nerd Font"
        font.pixelSize: 13
        color: "#c7c7c7"
        opacity: 0.4
    }
}
