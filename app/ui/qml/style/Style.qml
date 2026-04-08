pragma Singleton
import QtQuick

QtObject {
    id: root

    readonly property var themes: ({
        "dark": {
            "backgroundColor":     "#292b31",
            "buttonLighterColor":  "#187DF0",
            "buttonDarkerColor":   "#0C3F78",
            "borderColor":         "#4A4F5A",
            "fieldColor":          "#4A4F5A",
            "fontColor":           "#F5F5F5",
            "fontFamily":           "Roboto"
        }
    })

    property string activeTheme: 'dark'
    readonly property var current: themes[activeTheme]

    readonly property color backgroundColor:     current.backgroundColor
    readonly property color buttonLighterColor:  current.buttonLighterColor
    readonly property color buttonDarkerColor:   current.buttonDarkerColor
    readonly property color borderColor:         current.borderColor
    readonly property color fieldColor:          current.fieldColor
    readonly property color fontColor:           current.fontColor
    readonly property string fontFamily:         current.fontFamily
    

    function setTheme(name) {
        if (themes[name] !== undefined)
            activeTheme = name
    }
}