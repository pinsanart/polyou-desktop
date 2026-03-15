class Flashcard {
    #id

    #frontHTML
    #backHTML
    
    #language
    #type

    #audiosFilenames
    #imagesFilenames

    constructor(
        frontHTML = '',
        backHTML = '',
        language = '',
        type = '',
        audiosFilenames = [],
        imagesFilenames = []
    ) {
        this.#id = crypto.randomUUID()

        this.#frontHTML = frontHTML
        this.#backHTML = backHTML
        this.#language = language
        this.#type = type

        this.#audiosFilenames = [...audiosFilenames]
        this.#imagesFilenames = [...imagesFilenames]
    }

    get id() { return this.#id }
    get frontHTML() { return this.#frontHTML }
    get backHTML() { return this.#backHTML }
    get language() { return this.#language }
    get type() { return this.#type }

    get audioFilenames() { return [...this.#audiosFilenames] }
    get imagesFilenames() { return [...this.#imagesFilenames] }

    set frontHTML(value) { this.#frontHTML = value }
    set backHTML(value) { this.#backHTML = value }
    set language(value) { this.#language = value }
    set type(value) { this.#type = value }

    addImage(filename) {
        this.#imagesFilenames.push(filename)
    }

    addAudio(filename) {
        this.#audiosFilenames.push(filename)
    }

    removeImage(filename) {
        this.#imagesFilenames =
            this.#imagesFilenames.filter(f => f !== filename)
    }

    removeAudio(filename) {
        this.#audiosFilenames =
            this.#audiosFilenames.filter(f => f !== filename)
    }

    toJSON() {
        return {
            frontHTML: this.#frontHTML,
            backHTML: this.#backHTML,
            type: this.#type,
            language: this.#language,
            imagesFilenames: [...this.#imagesFilenames],
            audiosFilenames: [...this.#audiosFilenames]
        }
    }

    setByJSON(jsonData) {
        this.#frontHTML = jsonData.frontHTML ?? ""
        this.#backHTML = jsonData.backHTML ?? ""
        this.#language = jsonData.language ?? ""
        this.#type = jsonData.type ?? ""
        this.#imagesFilenames = [...(jsonData.imagesFilenames ?? [])]
        this.#audiosFilenames = [...(jsonData.audiosFilenames ?? [])]
    }
}