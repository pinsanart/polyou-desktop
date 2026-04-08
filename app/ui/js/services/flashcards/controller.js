class FlashcardControllerService {
    #container
    #editorStateService
    #flashcardCollection
    #flashcardViewFactory
    #mediaService

    #eventHandlers = {
        [FlashcardView.Events.FIELD_CHANGE]:    ({detail}) => this.#onFieldChange(detail),
        [FlashcardView.Events.MEDIA_ADD]:       ({detail}) => this.#onMediaAdd(detail),
        [FlashcardView.Events.MEDIA_REMOVE]:    ({detail}) => this.#onMediaRemove(detail),

        [FlashcardView.Events.COPY]:            ({detail}) => this.#onCopy(detail),
        [FlashcardView.Events.MOVE_UP]:         ({detail}) => this.#onMoveUp(detail),
        [FlashcardView.Events.MOVE_DOWN]:       ({detail}) => this.#onMoveDown(detail),
        [FlashcardView.Events.ADD_UP]:          ({detail}) => this.#onAddUp(detail),
        [FlashcardView.Events.ADD_DOWN]:        ({detail}) => this.#onAddDown(detail),
        [FlashcardView.Events.DELETE]:          ({detail}) => this.#onDelete(detail)

    }

    constructor(container, editorStateService, mediaService) {
        this.#container = container
        this.#editorStateService = editorStateService
        this.#mediaService = mediaService
        this.#flashcardViewFactory = new FlashcardViewFactory(mediaService)
    }

    async init() {
        this.#flashcardCollection = await this.#editorStateService.getCollection()
    }

    async render() {
        this.#container.innerHTML = ''
        
        for (const flashcard of this.#flashcardCollection) {
            const flashcardView = await this.#createFlaschardView(flashcard)

            this.#container.appendChild(flashcardView.create())
        }
    }

    async #createFlaschardView(flashcard) {
        const flashcardView = await this.#flashcardViewFactory.create(flashcard)

        this.#bindFlashcardViewEvents(flashcardView) 

        return flashcardView
    }

    #bindFlashcardViewEvents(flashcardView) {
        for (const [event, handler] of Object.entries(this.#eventHandlers)) {
            flashcardView.addEventListener(event, handler)
        }
    }
    
    async #onFieldChange({flashcardId, field, html}) {
        const flashcard = this.#flashcardCollection.findById(flashcardId)
        if (!flashcard) return

        if (field === FlashcardView.FieldNames.FRONT) flashcard.frontText = html
        if (field === FlashcardView.FieldNames.BACK) flashcard.backText = html

        await this.#editorStateService.saveCollection(this.#flashcardCollection)
    }

    async #onMediaAdd({flashcardId, mediaId, field, type, file}) {
        const flashcard = this.#flashcardCollection.findById(flashcardId)
        if (!flashcard) return

        const filename = await this.#mediaService.saveFile(file, mediaId)

        if (field === FlashcardView.FieldNames.FRONT) {
            if (type === FlashcardView.MediaTypes.IMAGE) flashcard.addFrontImage(filename)
            if (type === FlashcardView.MediaTypes.AUDIO) flashcard.addFrontAudio(filename)
        }
        if (field === FlashcardView.FieldNames.BACK) {
            if (type === FlashcardView.MediaTypes.IMAGE) flashcard.addBackImage(filename)
            if (type === FlashcardView.MediaTypes.AUDIO) flashcard.addBackAudio(filename)
        }

        this.#editorStateService.saveCollection(this.#flashcardCollection)
    }

    async #onMediaRemove({flashcardId, mediaId, field, type}) {
        const flashcard = this.#flashcardCollection.findById(flashcardId)
        if (!flashcard) return

        const filename = this.#mediaService.removeByMediaId(mediaId)
        if (!filename) return

        if (field === FlashcardView.FieldNames.FRONT) {
            if (type === FlashcardView.MediaTypes.IMAGE) flashcard.removeFrontImage(filename)
            if (type === FlashcardView.MediaTypes.AUDIO) flashcard.removeFrontAudio(filename)
        }
        if (field === FlashcardView.FieldNames.BACK) {
            if (type === FlashcardView.MediaTypes.IMAGE) flashcard.removeBackImage(filename)
            if (type === FlashcardView.MediaTypes.AUDIO) flashcard.removeBackAudio(filename)
        }

        this.#editorStateService.saveCollection(this.#flashcardCollection)
    }
    
    #onCopy({flashcardId}) {
        
    }

    #onMoveUp({flashcardId}) {

    }

    #onMoveDown({flashcardId}) {

    }

    #onAddUp({flashcardId}) {

    }

    #onAddDown({flashcardId}) {
        
    }

    #onDelete({flashcardId}) {
        this.#flashcardCollection.removeById(flashcardId)        
    }
}