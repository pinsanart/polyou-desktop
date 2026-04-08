class MediaBridge {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const objects = await Channel.init()
        if (!objects.mediaBridge) { reject("The object 'mediaBridge' was not exposed by WebChannel"); return }
        this.mediaBridge = objects.mediaBridge
        resolve(this.mediaBridge)
    }

    async save(base64_data, mime_type) {
        const mediaBridge = await this.#ready
        return new Promise((resolve) => {
            mediaBridge.save(base64_data, mime_type, (filename) => {
                resolve(filename)
            })

        })         
    }

    async get(filename) {
        const mediaBridge = await this.#ready
        return new Promise((resolve) => {
            mediaBridge.get(filename, (dataURL) => {
                resolve(dataURL)
            })
        })
    }

    async delete(filename) {
        const mediaBridge = await this.#ready
        return new Promise((resolve) => {
            mediaBridge.get(filename, (result) => {
                resolve(result)
            })
        })
    }

    async isReady() {
        return this.#ready
    }
}