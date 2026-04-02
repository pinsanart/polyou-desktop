class FlashcardViewModel {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const objects = await Channel.init()
        if (!objects.flashcardViewModel) { reject("The object 'flashcardViewModel' was not exposed by WebChannel"); return }
        this.flashcardViewModel = objects.flashcardViewModel
        resolve(this.flashcardViewModel)
    }

    async create_one(data) {
        const flashcardViewModel = await this.#ready
        flashcardViewModel.create_one(data)
    }

    async create_many(data) {
        const flashcardViewModel = await this.#ready
        flashcardViewModel.create_many(data)
    }

    async isReady() {
        return this.#ready
    }
}