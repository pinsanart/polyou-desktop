class FlashcardView extends EventTarget {
    static Events = {
        FIELD_CHANGE: 'fieldChange',
        
        MEDIA_ADD: 'mediaAdd',
        MEDIA_REMOVE: 'mediaRemove',

        COPY: 'copy',
        MOVE_UP: 'moveUp',
        MOVE_DOWN: 'moveDown',
        ADD_UP: 'addUp',
        ADD_DOWN: 'addDown',
        DELETE: 'delete'
    }

    static FieldNames = {
        FRONT: "front",
        BACK: "back"
    }

    static MediaTypes = {
        IMAGE: { name: "image", HTMLTag: "img" },
        AUDIO: { name: "audio", HTMLTag: "audio"}
    }

    constructor() {
        super()
    }

    dispatchFieldChange({flashcardId, field, html}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.FIELD_CHANGE, {
            detail: {
                flashcardId, field, html
            }
        }))
    }

    dispatchMediaAdd({flashcardId, mediaId, field, type, file}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.MEDIA_ADD, {
            detail: {
                flashcardId, mediaId, field, type, file
            }
        }))    
    }

    dispatchMediaRemove({flashcardId, mediaId, field, type}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.MEDIA_REMOVE, {
            detail: { flashcardId, mediaId, field, type }
        }))
    }

    dispatchCopy({flashcardId}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.COPY, {
            detail: {
                flashcardId
            }
        }))
    }

    dispatchMoveUp({flashcardId}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.MOVE_UP), {
            detail: {
                flashcardId
            }
        })
    }

    dispatchMoveDown({flashcardId}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.MOVE_DOWN), {
            detail: {
                flashcardId
            }
        })
    }

    dispatchAddUp({flashcardId}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.ADD_UP), {
            detail: {
                flashcardId
            }
        })
    }

    dispatchAddDown({flashcardId}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.ADD_DOWN), {
            detail: {
                flashcardId
            }
        })
    }
  
    dispatchDelete({flashcardId}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.DELETE), {
            detail: {
                flashcardId
            }
        })
    }
 
    create() {
        throw new Error('create() must be implemented by subclass')
    }

    createControlBar() {
        const controls = document.createElement('div')
        controls.classList.add('flashcard-control-bar')

        const buttons = [
            { action: 'copy',      iconURL: 'qrc:assets/images/copy_icon.svg'},
            { action: 'move-up',   iconURL: 'qrc:assets/images/arrow_up_icon.svg'},
            { action: 'move-down', iconURL: 'qrc:assets/images/arrow_down_icon.svg'},
            { action: 'add-up',    iconURL: 'qrc:assets/images/cell_insert_above_icon.svg'},
            { action: 'add-down',  iconURL: 'qrc:assets/images/cell_insert_below_icon.svg'},
            { action: 'delete',    iconURL: 'qrc:assets/images/trash_icon.svg'},
        ]

        buttons.forEach(({ action, iconURL }) => {
            controls.appendChild(this.#createIconButton(action, iconURL))
        })

        return controls
    }

    #createIconButton(action, iconURL) {
        const button = document.createElement('button')
        button.classList.add('flashcard-control-btn', `flashcard-control-btn--${action}`)
        button.setAttribute('data-action', action)

        const icon = document.createElement('img')
        icon.src = iconURL
        icon.classList.add('flashcard-control-icon')
        button.appendChild(icon)
        return button
    }
}