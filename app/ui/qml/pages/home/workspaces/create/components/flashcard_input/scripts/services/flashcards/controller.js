class FlashcardControllerService {
    #container
    #editorStateService
    #flashcardCollection
    #flashcardViewFactory

    constructor(container, editorStateService, flashcardViewFactory) {
        this.#container = container
        this.#editorStateService = editorStateService
        this.#flashcardViewFactory = flashcardViewFactory
    }

    async init() {
        this.#flashcardCollection = await this.#editorStateService.getCollection()
    }

    async render() {
        this.#container.innerHTML = ''
        
        for (const flashcard of this.#flashcardCollection) {
            const flashcardView = await this.#flashcardViewFactory.create(flashcard)

            flashcardView.addEventListener(FlashcardView.Events.FIELD_CHANGE, (event) => {
                this.#onFieldChange(event.detail)
            })

            this.#container.appendChild(flashcardView.create())
        }
    }

    #onFieldChange({flashcardId, field, html}) {
        const flashcard = this.#flashcardCollection.findById(flashcardId)
        if (!flashcard) return

        if (field === 'front') flashcard.frontHTML = html
        if (field === 'back') flashcard.backHTML = html
    }
}