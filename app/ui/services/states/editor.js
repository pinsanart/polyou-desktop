class EditorStateService {
    #editorState

    constructor(editorState) {
        this.#editorState = editorState
    }

    async saveCollection(flashcardCollection) {
        await this.#editorState.saveFlashcards(flashcardCollection.toJSON())
    }

    async getCollection() {
        const data = await this.#editorState.getFlashcards()
        return new FlashcardCollectionService(data)
    }
}