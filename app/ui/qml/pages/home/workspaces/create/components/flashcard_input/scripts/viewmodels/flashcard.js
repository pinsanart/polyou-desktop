class FlashcardViewModel {
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
                    const flashcardViewModel = channel.objects.flashcardViewModel
                    if (!flashcardViewModel) {
                        reject("The object 'flashcardViewModel' was not exposed by WebChannel")
                        return
                    }
                    
                    this.flashcardViewModel = flashcardViewModel

                    resolve(this.flashcardViewModel)
                })
            } else {
               setTimeout(tryInit, 100);
            }
        } 

        tryInit()
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