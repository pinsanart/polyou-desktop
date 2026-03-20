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

    dispatchFieldChange({flashcardId, field, html}) {
        this.dispatchEvent(new CustomEvent(FlashcardView.Events.FIELD_CHANGE, {
            detail: {
                flashcardId, field, html
            }
        }))
    }

    constructor() {
        super()
    }

    create() {
        throw new Error('create() must be implemented by subclass')
    }

    createControlBar() {
        const controls = document.createElement('div')
        controls.classList.add('flashcard-control-bar')

        const buttons = [
            { action: 'copy',      iconURL: 'qrc:/images/copy_icon.svg'},
            { action: 'move-up',   iconURL: 'qrc:/images/arrow_up_icon.svg'},
            { action: 'move-down', iconURL: 'qrc:/images/arrow_down_icon.svg'},
            { action: 'add-up',    iconURL: 'qrc:/images/cell_insert_above_icon.svg'},
            { action: 'add-down',  iconURL: 'qrc:/images/cell_insert_below_icon.svg'},
            { action: 'delete',    iconURL: 'qrc:/images/trash_icon.svg'},
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