class FlashcardCollection {

    #flashcards = []
    #flashcardsById = new Map()

    constructor(jsonData = {}) {
        if (!jsonData.flashcards || jsonData.flashcards.length === 0) {
            const card = new Flashcard()
            this.#insert(card)
            return
        }

        for (const data of jsonData.flashcards) {
            const card = new Flashcard()
            card.setByJSON(data)
            this.#insert(card)
        }
    }

    #insert(card, index = null) {
        if (index === null || index >= this.#flashcards.length) {
            this.#flashcards.push(card)
        } else {
            this.#flashcards.splice(index, 0, card)
        }

        this.#flashcardsById.set(card.id, card)
    }

    add(index, jsonData = {}) {
        const card = new Flashcard()
        if (Object.keys(jsonData).length) {
            card.setByJSON(jsonData)
        }

        this.#insert(card, index)
        return card
    }

    push(jsonData = {}) {
        return this.add(this.#flashcards.length, jsonData)
    }

    get(index) {
        return this.#flashcards[index] ?? null
    }

    findById(id) {
        return this.#flashcardsById.get(id) ?? null
    }

    indexOfId(id) {
        const card = this.#flashcardsById.get(id)
        if (!card) return -1
        return this.#flashcards.indexOf(card)
    }

    removeByIndex(index) {
        if (index < 0 || index >= this.#flashcards.length) {
            return false
        }

        const card = this.#flashcards[index]

        this.#flashcards.splice(index, 1)
        this.#flashcardsById.delete(card.id)

        return true
    }

    removeById(id) {
        const card = this.#flashcardsById.get(id)
        if (!card) return false

        const index = this.#flashcards.indexOf(card)

        this.#flashcards.splice(index, 1)
        this.#flashcardsById.delete(id)

        return true
    }

    move(oldIndex, newIndex) {
        if (
            oldIndex < 0 || oldIndex >= this.#flashcards.length ||
            newIndex < 0 || newIndex >= this.#flashcards.length
        ) {
            return false
        }

        const [card] = this.#flashcards.splice(oldIndex, 1)
        this.#flashcards.splice(newIndex, 0, card)

        return true
    }

    replace(index, jsonData) {
        if (index < 0 || index >= this.#flashcards.length) {
            return false
        }

        const old = this.#flashcards[index]

        const card = new Flashcard()
        card.setByJSON(jsonData)

        this.#flashcards[index] = card

        this.#flashcardsById.delete(old.id)
        this.#flashcardsById.set(card.id, card)

        return true
    }

    clear() {
        this.#flashcards = []
        this.#flashcardsById.clear()
    }

    length() {
        return this.#flashcards.length
    }

    isEmpty() {
        return this.#flashcards.length === 0
    }

    map(callback) {
        return this.#flashcards.map(callback)
    }

    filter(callback) {
        return this.#flashcards.filter(callback)
    }

    forEach(callback) {
        this.#flashcards.forEach(callback)
    }

    toJSON() {
        return {
            flashcards: this.#flashcards.map(f => f.toJSON())
        }
    }

    [Symbol.iterator]() {
        return this.#flashcards[Symbol.iterator]()
    }
}