class MediaViewModel {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const objects = await Channel.init()
        if (!objects.mediaViewModel) { reject("The object 'mediaViewModel' was not exposed by WebChannel"); return }
        this.mediaViewModel = objects.mediaViewModel
        resolve(this.mediaViewModel)
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