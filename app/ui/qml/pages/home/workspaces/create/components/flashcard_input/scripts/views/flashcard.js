class FlashcardView extends EventTarget {
    #initialData

    constructor(flashcardInitialData) {
        super()
        this.#initialData= flashcardInitialData
    }

    get initialData() {
        return this.#initialData
    }
}