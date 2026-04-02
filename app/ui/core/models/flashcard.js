class Flashcard {
    #id
    #frontText
    #backText
    #language
    #type

    #frontAudiosFilenames
    #frontImagesFilenames

    #backAudiosFilenames
    #backImagesFilenames

    constructor(
        frontText = '',
        backText = '',
        language = '',
        type = '',
        frontImagesFilenames = [],
        frontAudiosFilenames = [],
        backImagesFilenames = [],
        backAudiosFilenames = []

    ) {
        this.#id = crypto.randomUUID()
        this.#frontText = frontText
        this.#backText = backText
        this.#language = language
        this.#type = type

        this.#frontImagesFilenames = [...frontImagesFilenames]
        this.#frontAudiosFilenames = [...frontAudiosFilenames]
        this.#backAudiosFilenames = [...backAudiosFilenames]
        this.#backImagesFilenames = [...backImagesFilenames]
    }

    get id() { return this.#id }
    get frontText() { return this.#frontText }
    get backText() { return this.#backText }
    get language() { return this.#language }
    get type() { return this.#type }

    get frontImagesFilenames() { return [...this.#frontImagesFilenames] }
    get frontAudiosFilenames() { return [...this.#frontAudiosFilenames] }
    get backAudiosFilenames() { return [...this.#backAudiosFilenames] }
    get backImagesFilenames() { return [...this.#backImagesFilenames] }

    set frontText(value) { this.#frontText = value }
    set backText(value) { this.#backText = value }
    set language(value) { this.#language = value }
    set type(value) { this.#type = value }

    addFrontImage(filename) {
        this.#frontImagesFilenames.push(filename)
    }

    addFrontAudio(filename) {
        this.#frontAudiosFilenames.push(filename)
    }

    removeFrontImage(filename) {
        this.#frontImagesFilenames =
            this.#frontImagesFilenames.filter(f => f !== filename)
    }

    removeFrontAudio(filename) {
        this.#frontAudiosFilenames =
            this.#frontAudiosFilenames.filter(f => f !== filename)
    }

    addBackImage(filename) {
        this.#backImagesFilenames.push(filename)
    }

    addBackAudio(filename) {
        this.#backAudiosFilenames.push(filename)
    }

    removeBackImage(filename) {
        this.#backImagesFilenames =
            this.#backImagesFilenames.filter(f => f !== filename)
    }

    removeBackAudio(filename) {
        this.#backAudiosFilenames =
            this.#backAudiosFilenames.filter(f => f !== filename)
    }

    toJSON() {
        return {
            id: this.#id,
            frontText: this.#frontText,
            backText: this.#backText,
            type: this.#type,
            language: this.#language,
            
            frontImagesFilenames: [...this.#frontImagesFilenames],
            frontAudiosFilenames: [...this.#frontAudiosFilenames],
            backImagesFilenames: [...this.#backImagesFilenames],
            backAudiosFilenames: [...this.#backAudiosFilenames]
        }
    }

    setByJSON(jsonData) {
        this.#id = jsonData.id ?? crypto.randomUUID()
        this.#frontText = jsonData.frontText ?? ""
        this.#backText = jsonData.backText ?? ""
        this.#language = jsonData.language ?? ""
        this.#type = jsonData.type ?? ""

        this.#frontImagesFilenames = [...(jsonData.frontImagesFilenames ?? [])]
        this.#frontAudiosFilenames = [...(jsonData.frontAudiosFilenames ?? [])]
        this.#backImagesFilenames = [...(jsonData.backImagesFilenames ?? [])]
        this.#backAudiosFilenames = [...(jsonData.backAudiosFilenames ?? [])]
    }
}