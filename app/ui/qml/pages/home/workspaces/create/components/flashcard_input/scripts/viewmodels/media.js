class MediaViewModel {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const tryInit = () => {
            if (window.qt && qt.webChannelTransport) {
                new QWebChannel(qt.webChannelTransport, (channel) => {
                    const mediaViewModel = channel.objects.mediaViewModel
                    if (!mediaViewModel) {
                        reject("The object 'mediaViewModel' was not exposed by WebChannel")
                        return
                    }
                    
                    this.mediaViewModel = mediaViewModel

                    resolve(this.mediaViewModel)
                })
            } else {
               setTimeout(tryInit, 100);
            }
        } 

        tryInit()
    }

    async save(base64_data, mime_type) {
        const mediaViewModel = await this.#ready
        return new Promise((resolve) => {
            mediaViewModel.save(base64_data, mime_type, (filename) => {
                resolve(filename)
            })

        })         
    }

    async get(filename) {
        const mediaViewModel = await this.#ready
        return new Promise((resolve) => {
            mediaViewModel.get(filename, (dataURL) => {
                resolve(dataURL)
            })
        })
    }

    async isReady() {
        return this.#ready
    }
}