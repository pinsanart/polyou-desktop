class EditorState {
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
                    const editorState = channel.objects.editorState
                    if (!editorState) {
                        reject("The object 'editorState' was not exposed by WebChannel")
                        return
                    }
                    
                    this.editorState = editorState

                    resolve(this.editorState)
                })
            } else {
               setTimeout(tryInit, 100);
            }
        }

        tryInit()
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