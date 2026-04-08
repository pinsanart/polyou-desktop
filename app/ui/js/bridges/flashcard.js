class FlashcardBridge {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const objects = await Channel.init()
        if (!objects.flashcardBridge) { reject("The object 'flashcardBridge' was not exposed by WebChannel"); return }
        this.flashcardBridge = objects.flashcardBridge
        resolve(this.flashcardBridge)
    }

    async create_one(data) {
        const flashcardBridge = await this.#ready
        flashcardBridge.create_one(data)
    }

    async create_many(data) {
        const flashcardBridge = await this.#ready
        flashcardBridge.create_many(data)
    }

    async isReady() {
        return this.#ready
    }
}