class FlashcardView extends EventTarget {
    #initialData
    #medias

    static Events = {
        FIELD_CHANGE: 'fieldChange',
        MEDIA_ADD: 'mediaAdd',
        MEDIA_REMOVE: 'mediaRemove'
    }

    constructor(flashcardInitialData, medias) {
        super()
        this.#initialData= flashcardInitialData
        this.#medias = medias
    }

    get initialData() {
        return this.#initialData
    }

    dispatchFieldChange(side, html) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.FIELD_CHANGE, {
            detail: { flashcardId: this.initialData.id, side, html }
        }))
    }

    dispatchMediaAdd(mediaId, file) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.MEDIA_ADD, {
            detail: {flashcardId: this.initialData.id, mediaId, file}
        }))
    }

    dispatchMediaRemove(mediaId) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.MEDIA_REMOVE, {
            detail: {flashcardId: this.initialData.id, mediaId}
        }))
    }
}