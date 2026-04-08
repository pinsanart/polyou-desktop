class EditorStateService {
    #editorStateBridge

    constructor(editorState) {
        this.#editorStateBridge = editorState
    }

    async saveCollection(flashcardCollection) {
        await this.#editorStateBridge.saveFlashcards(flashcardCollection.toJSON())
    }

    async getCollection() {
        const data = await this.#editorStateBridge.getFlashcards()
        return new FlashcardCollectionService(data)
    }
}