const Channel = (() => {
    let _ready

    function init() {
        if (_ready) return _ready

        _ready = new Promise((resolve, reject) => {
            const tryInit = () => {
                if (window.qt && qt.webChannelTransport) {
                    new QWebChannel(qt.webChannelTransport, (channel) => {
                        resolve(channel.objects)
                    })
                } else {
                    setTimeout(tryInit, 100)
                }
            }
            tryInit()
        })

        return _ready
    }

    return { init }
})()