class FlashcardView extends EventTarget {
    static Events = {
        FIELD_CHANGE: 'fieldChange',
        MEDIA_ADD: 'mediaAdd',
        MEDIA_REMOVE: 'mediaRemove'
    }

    constructor() {
        super()
    }

    create() {
        throw new Error('create() must be implemented by subclass')
    }

    dispatchFieldChange(fieldName, html) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.FIELD_CHANGE, {
            detail: { flashcardId: this.initialData.id, fieldName, html }
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