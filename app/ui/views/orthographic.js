class OrthographicView extends FlashcardView {
    #flashcardId
    #initialAudioText
    #initialAudioMedia

    static FIELDS = {
        AUDIO: {
            name: FlashcardView.FieldNames.FRONT,
            label: "Audio",
            getAudioText: (ctx) => ctx.#initialAudioText,
            getAudioMedia: (ctx) => ctx.#initialAudioMedia
        }
    }

    constructor(flascahrdId, initialAudioText = '', initialAudioMedia) {
        super()
        this.#flashcardId = flascahrdId
        this.initialAudioText = initialAudioText
        this.#initialAudioMedia = initialAudioMedia
    }

    create() {
        const wrapper = document.createElement('div')
        wrapper.classList.add('wrapper-flashcard-control', 'orthographic-wrapper-flashcard-control')
        
        wrapper.appendChild(this.createControlBar())
        
        const cardEditor = document.createElement('div')
        cardEditor.classList.add('card-editor', 'orthographic-card-editor')

        const body = document.createElement('div')
        body.classList.add('card-body', 'ortographic-card-body')

        cardEditor.appendChild(body)
        wrapper.appendChild(cardEditor)

        return wrapper
    }
}