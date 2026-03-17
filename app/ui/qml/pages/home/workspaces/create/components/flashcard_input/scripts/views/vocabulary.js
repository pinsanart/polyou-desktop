class VocabularyView extends FlashcardView {
    constructor(flashcardInitialData) {
        super(flashcardInitialData)
    }

    create(frontLabel = 'Front', backLabel = 'Back') {
        const cardEditor = document.createElement('div')
        cardEditor.classList.add('card-editor')

        const body = document.createElement('div')
        body.classList.add('card-body')

        body.appendChild(this.#createField('front', frontLabel, this.initialData.frontHTML))
        body.appendChild(this.#createField('back', backLabel, this.initialData.backHTML))

        cardEditor.appendChild(body)
        
        return cardEditor
    }

    #createField(side, label, initialHTML = '') {
        const fieldRow = document.createElement('div')
        fieldRow.classList.add('field-row')

        fieldRow.appendChild(this.#createFieldHeader(label))
        fieldRow.appendChild(this.#createFieldModes(side, initialHTML))
        fieldRow.appendChild(this.#createFieldMedia())

        return fieldRow
    }

    #createFieldHeader(label) {
        const header = document.createElement('div')
        header.classList.add('field-header')

        const fieldLabel = document.createElement('span')
        fieldLabel.classList.add('field-label')
        fieldLabel.textContent = label

        header.appendChild(fieldLabel)

        return header
    }

    #createFieldModes(side, initialHTML = '') {
        const fieldMode = document.createElement('div')
        fieldMode.classList.add('field-modes')

        const editor = document.createElement('div')
        editor.classList.add('editor-area')
        editor.contentEditable = 'true'
        editor.innerHTML = initialHTML
        
        fieldMode.appendChild(editor)

        const HTMLArea = document.createElement('textarea')
        HTMLArea.classList.add('html-area')
        HTMLArea.spellcheck = false
        HTMLArea.textContent = initialHTML

        editor.addEventListener('input', () => {
            HTMLArea.value = editor.innerHTML
            this.dispatchFieldChange(side, editor.innerHTML)
        })


        HTMLArea.addEventListener('input', () => {
            editor.innerHTML = HTMLArea.value
            this.dispatchFieldChange(side, HTMLArea.value)
        })

        fieldMode.appendChild(HTMLArea)

        return fieldMode
    }

    #createFieldMedia() {
        const fieldMedia = document.createElement('div')
        fieldMedia.classList.add('field-media')

        fieldMedia.appendChild(this.#createMediaRow('image', 'image/*'))
        fieldMedia.appendChild(this.#createMediaRow('audio', 'audio/*'))

        return fieldMedia
    }

    #createMediaRow(type, accept) {
        const row = document.createElement('div')
        row.classList.add(`${type}-row`)

        const label = document.createElement('span')
        label.classList.add(`${type}-label`)
        label.textContent = `${type}s`

        row.appendChild(label)
        const input = document.createElement('input')
        input.classList.add(`input-${type}`)
        input.type = 'file'
        input.accept = accept

        const preview = document.createElement('div')
        preview.classList.add(`${type}s-preview`)

        const previewLabel = document.createElement('span')
        previewLabel.classList.add(`${type}s-preview-label`)
        previewLabel.textContent = 'preview'
        preview.appendChild(previewLabel)

        input.addEventListener('change', () => {
            Array.from(input.files).forEach((file) => {
                preview.appendChild(this.#createPreviewItem(type, file))
            })
        })

        row.appendChild(input)
        row.appendChild(preview)

        return row
    }

    #createPreviewItem(type, file) {
        const mediaId = crypto.randomUUID()

        const url = URL.createObjectURL(file)
        const tag = type === 'image' ? 'img' : type

        const wrapper = document.createElement('div')
        wrapper.classList.add(`${type}-wrapper`)
        wrapper.dataset.mediaId = mediaId

        const media = document.createElement(tag)
        media.classList.add(`${type}-preview`)
        media.src = url
        if (type === 'audio') media.controls = true

        const button = document.createElement('button')
        button.classList.add(`remove-${type}-button`)
        button.innerHTML = 'X'
        button.addEventListener('click', () => wrapper.remove())
    
        wrapper.appendChild(button)
        wrapper.appendChild(media)

        return wrapper
    }
}