class Flashcard {
    #frontHTML
    #backHTML    
    #audiosFilenames
    #imagesFilenames

    constructor(frontHTML = '', backHTML = '', audiosFilenames = [], imagesFilenames = []) {
        this.#frontHTML = frontHTML
        this.#backHTML = backHTML
        this.#audiosFilenames = audiosFilenames
        this.#imagesFilenames = imagesFilenames
    }

    get frontHTML() { return this.#frontHTML }
    get backHTML() { return this.#backHTML }
    get audioFilenames() { return [...this.#audiosFilenames] }
    get imagesFilenames() { return [...this.#imagesFilenames] }

    set frontHTML(frontHTML) { this.#frontHTML = frontHTML }
    set backHTML(backHTML) { this.#backHTML = backHTML }
    
    addImage(filename) {
        this.#imagesFilenames.push(filename)
    }
    
    addAudio(filename) {
        this.#audiosFilenames.push(filename)
    }

    removeImage(filename) {
        this.#imagesFilenames = this.#imagesFilenames.filter(f => f !== filename)
    }

    removeAudio(filename) {
        this.#audiosFilenames = this.#imagesFilenames.filter(f => f !== filename)
    }

    toJSON() {
        return {
            frontHTML:          this.#frontHTML,
            backHTML:           this.#backHTML,
            imagesFilenames:    this.#imagesFilenames,
            audiosFilenames:    this.#audiosFilenames
        }
    }

    setByJSON(jsonData) {
        this.#frontHTML       = jsonData.frontHTML ?? ""
        this.#backHTML        = jsonData.backHTML ?? ""
        this.#imagesFilenames = jsonData.imagesFilenames ?? []
        this.#audiosFilenames = jsonData.audiosFilenames ?? []
    }
}