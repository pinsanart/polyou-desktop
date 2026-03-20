class Flashcard {
    #id
    #frontHTML
    #backHTML
    #language
    #type

    #frontAudiosFilenames
    #frontImagesFilenames

    #backAudiosFilenames
    #backImagesFilenames

    constructor(
        frontHTML = '',
        backHTML = '',
        language = '',
        type = '',
        frontImagesFilenames = [],
        frontAudiosFilenames = [],
        backImagesFilenames = [],
        backAudiosFilenames = []

    ) {
        this.#id = crypto.randomUUID()
        this.#frontHTML = frontHTML
        this.#backHTML = backHTML
        this.#language = language
        this.#type = type

        this.#frontImagesFilenames = [...frontImagesFilenames]
        this.#frontAudiosFilenames = [...frontAudiosFilenames]
        this.#backAudiosFilenames = [...backAudiosFilenames]
        this.#backImagesFilenames = [...backImagesFilenames]
    }

    get id() { return this.#id }
    get frontHTML() { return this.#frontHTML }
    get backHTML() { return this.#backHTML }
    get language() { return this.#language }
    get type() { return this.#type }

    get frontImagesFilenames() { return [...this.#frontImagesFilenames] }
    get frontAudiosFilenames() { return [...this.#frontAudiosFilenames] }
    get backAudiosFilenames() { return [...this.#backAudiosFilenames] }
    get backImagesFilenames() { return [...this.#backImagesFilenames] }

    set frontHTML(value) { this.#frontHTML = value }
    set backHTML(value) { this.#backHTML = value }
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
            frontHTML: this.#frontHTML,
            backHTML: this.#backHTML,
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
        this.#frontHTML = jsonData.frontHTML ?? ""
        this.#backHTML = jsonData.backHTML ?? ""
        this.#language = jsonData.language ?? ""
        this.#type = jsonData.type ?? ""

        this.#frontImagesFilenames = [...(jsonData.frontImagesFilenames ?? [])]
        this.#frontAudiosFilenames = [...(jsonData.frontAudiosFilenames ?? [])]
        this.#backImagesFilenames = [...(jsonData.backImagesFilenames ?? [])]
        this.#backAudiosFilenames = [...(jsonData.backAudiosFilenames ?? [])]
    }
}