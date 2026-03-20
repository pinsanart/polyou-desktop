class EditorState {
    #ready

    constructor() {
        this.#ready = new Promise((resolve, reject) => {
            this.#init(resolve, reject)
        })
    }

    async #init(resolve, reject) {
        const objects = await Channel.init()
        if (!objects.editorState) { reject("The object 'editorState' was not exposed by WebChannel"); return }
        this.editorState = objects.editorState
        resolve(this.editorState)
    }

    async saveFlashcards(data) {
        const editorState = await this.#ready
        return await editorState.saveFlashcards(data)
    }

    async getFlashcards() {
        const editorState = await this.#ready
        return new Promise((resolve) => {
            editorState.getFlashcards((data) => {
                resolve(data)
            })
        })        
    }

    async isReady() {
        return this.#ready
    }
}