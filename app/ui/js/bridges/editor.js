class EditorStateBridge {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const objects = await Channel.init()
        if (!objects.editorStateBridge) { reject("The object 'editorStateBridge' was not exposed by WebChannel"); return }
        this.editorStateBridge = objects.editorStateBridge
        resolve(this.editorStateBridge)
    }

    async saveFlashcards(data) {
        const editorStateBridge = await this.#ready
        return await editorStateBridge.saveFlashcards(data)
    }

    async getFlashcards() {
        const editorStateBridge = await this.#ready
        return new Promise((resolve) => {
            editorStateBridge.getFlashcards((data) => {
                resolve(data)
            })
        })        
    }

    async isReady() {
        return this.#ready
    }
}