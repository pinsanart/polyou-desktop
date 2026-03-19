class FlaschardViewControls {
    static #ICONS = {
        'copy':      'qrc:/images/copy_icon.svg',
        'move-up':   'qrc:/images/arrow_up_icon.svg',
        'move-down': 'qrc:/images/arrow_down_icon.svg',
        'add-up':    'qrc:/images/cell_insert_above_icon.svg',
        'add-down':  'qrc:/images/cell_insert_below_icon.svg',
        'delete':    'qrc:/images/trash_icon.svg',
    }

    static create(flaschardView) {
        const wrapper = document.createElement('div')
        wrapper.classList.add('wrapper-flashcard-control')

        wrapper.appendChild(this.#createControlBar())
        wrapper.appendChild(flaschardView.create())

        return wrapper
    }

    static #createControlBar() {
        const controls = document.createElement('div')
        controls.classList.add('flashcard-control-bar')

        const buttons = [
            { action: 'copy',      label: 'Copy' },
            { action: 'move-up',   label: 'Move Up' },
            { action: 'move-down', label: 'Move Down' },
            { action: 'add-up',    label: 'Add Above' },
            { action: 'add-down',  label: 'Add Below' },
            { action: 'delete',    label: 'Delete' },
        ]

        buttons.forEach(({ action, label }) => {
            controls.appendChild(this.#createButton(action, label))
        })

        return controls
    }

    static #createButton(action, label) {
        const button = document.createElement('button')
        button.classList.add('flashcard-control-btn', `flashcard-control-btn--${action}`)
        button.setAttribute('aria-label', label)
        button.setAttribute('title', label)
        button.setAttribute('data-action', action)

        const icon = document.createElement('img')
        icon.src = this.#ICONS[action]
        icon.alt = label
        icon.classList.add('flashcard-control-icon')
        button.appendChild(icon)

        return button
    }
}