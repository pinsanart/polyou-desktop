class FlashcardViewFactory {
    static #registry = {
        vocabulary: VocabularyView,
        pronounce: PronounceView,
        ortographic: OrtographicView
    }

    static create(card) {
        const viewClass = this.#registry[card.type]
        if (!viewClass) throw new Error(`Unknown flashcard type ${card.type}`)
        return new viewClass(card.toJSON())
    }

    static register(type, viewClass) {
        this.#registry[type] = viewClass
    }
}