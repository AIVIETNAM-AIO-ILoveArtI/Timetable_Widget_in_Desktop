import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
import QtWebSockets
import QtQuick.Window

Window {
    id: rootWindow
    width: Screen.width * 0.40 
    height: width * (1267.0 / 1291.0)
    visible: true
    color: "transparent"
    title: "NekoBox AI"

    // Xóa viền cửa sổ OS mặc định và luôn nổi trên cùng
    flags: Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window

    // Cho phép dùng chuột kéo cửa sổ đi bất cứ đâu
    DragHandler {
        target: rootWindow
    }

    Image {
        id: catImage
        source: "cat_cropped.png"
        anchors.fill: parent
        fillMode: Image.Stretch 
    }

    ListModel { id: chatHistoryModel }

    QtObject {
        id: internal
        function parseMessage(msg) {
            if (msg.startsWith("CHATBOT_RESPONSE:")) {
                var content = msg.substring(17);
                chatHistoryModel.append({
                    "sender": "Neko 🐾",
                    "message": content,
                    "isUser": false
                });
            }
        }
    }

    WebSocket {
        id: socket
        url: "ws://localhost:8080"
        active: true
        onTextMessageReceived: (message) => internal.parseMessage(message)
    }

    Rectangle {
        id: chatBox
        x: parent.width * 0.09
        y: parent.height * 0.52
        width: parent.width * 0.68
        height: parent.height * 0.43 
        
        color: "#1e1e2e" 
        radius: 12
        border.color: "#cba6f7"
        border.width: 2

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 10
            spacing: 8

            ScrollView {
                id: chatScrollView
                Layout.fillWidth: true
                Layout.fillHeight: true
                clip: true
                ScrollBar.vertical.policy: ScrollBar.AsNeeded

                ListView {
                    id: chatListView
                    model: chatHistoryModel
                    width: chatScrollView.width
                    spacing: 10
                    interactive: true
                    
                    delegate: Rectangle {
                        width: chatListView.width * 0.92
                        height: msgText.implicitHeight + 20
                        color: model.isUser ? "#313244" : "#45475a"
                        radius: 10
                        anchors.right: model.isUser ? parent.right : undefined
                        anchors.left: model.isUser ? undefined : parent.left

                        Text {
                            id: msgText
                            text: "<b>" + model.sender + ":</b> " + model.message
                            color: "#BAC2DE"
                            anchors.fill: parent
                            anchors.margins: 10
                            wrapMode: Text.WordWrap
                            font.pointSize: 9
                        }
                    }
                    onCountChanged: chatListView.currentIndex = count - 1
                }
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 35
                color: "#11111b"
                radius: 8

                TextField {
                    id: inputField
                    anchors.fill: parent
                    anchors.margins: 5
                    background: null
                    color: "#BAC2DE"
                    placeholderText: "Hỏi Neko gì đi meow..."
                    font.pointSize: 10
                    focus: true 
                    
                    onAccepted: {
                        if (text !== "") {
                            chatHistoryModel.append({
                                "sender": "Bạn",
                                "message": text,
                                "isUser": true
                            });
                            socket.sendTextMessage("SEND_PROMPT\n" + text);
                            text = "";
                        }
                    }
                }
            }
        }
    }
}
