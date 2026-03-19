class VocabularyView extends FlashcardView {
    #initialFrontHTML
    #initialBackHTML
    #initialFrontImagesMedia
    #initialFrontAudiosMedia
    #initialBackImagesMedia
    #initialBackAudiosMedia

    static MediaTypes = {
        IMAGE: { name: "image", HTMLTag: "img" },
        AUDIO: { name: "audio", HTMLTag: "audio"}
    }

    static Fields = {
        FRONT: {
            name: "front",
            label: "Front",
            getHTML: (ctx) => ctx.#initialFrontHTML,
            getImageMedia: (ctx) => ({type: VocabularyView.MediaTypes.IMAGE, value: ctx.#initialFrontImagesMedia}),
            getAudioMedia: (ctx) => ({type: VocabularyView.MediaTypes.AUDIO, value: ctx.#initialFrontAudiosMedia})
        },
        BACK: {
            name: "back", 
            label: "Back",
            getHTML: (ctx) => ctx.#initialBackHTML,
            getImageMedia: (ctx) => ({type: VocabularyView.MediaTypes.IMAGE, value: ctx.#initialBackImagesMedia}),
            getAudioMedia: (ctx) => ({type: VocabularyView.MediaTypes.AUDIO, value: ctx.#initialBackAudiosMedia})
        }
    }

    static setLabel(key, newLabel) {
        if (this.Fields[key]) {
            this.Fields[key].label = newLabel
        }
    }

    constructor(initialFrontHTML = '', initialBackHTML = '', initialFrontImagesMedia = [], initialFrontAudiosMedia = [], initialBackImagesMedia = [], initialBackAudiosMedia = []) {
        super()
        this.#initialFrontHTML = initialFrontHTML
        this.#initialBackHTML = initialBackHTML
        this.#initialFrontImagesMedia = initialFrontImagesMedia
        this.#initialFrontAudiosMedia = initialFrontAudiosMedia
        this.#initialBackImagesMedia = initialBackImagesMedia
        this.#initialBackAudiosMedia = initialBackAudiosMedia
    }

    create() {
        const cardEditor = document.createElement('div')
        cardEditor.classList.add('card-editor')

        const body = document.createElement('div')
        body.classList.add('card-body')

        body.appendChild(this.#createField(VocabularyView.Fields.FRONT))
        body.appendChild(this.#createField(VocabularyView.Fields.BACK))

        cardEditor.appendChild(body)
        
        return cardEditor
    }

    #createField(field) {
        const fieldRow = document.createElement('div')
        fieldRow.classList.add('field-row')

        fieldRow.appendChild(this.#createFieldHeader(field.label))
        fieldRow.appendChild(this.#createFieldModes(field.getHTML(this)))
        fieldRow.appendChild(this.#createFieldMedia(field))

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

    #createFieldModes(initialHTML) {
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
        })

        HTMLArea.addEventListener('input', () => {
            editor.innerHTML = HTMLArea.value
        })

        fieldMode.appendChild(HTMLArea)

        return fieldMode
    }

    #createFieldMedia(field) {
        const fieldMedia = document.createElement('div')
        fieldMedia.classList.add('field-media')

        fieldMedia.appendChild(this.#createMediaRow(field.getImageMedia(this)))
        fieldMedia.appendChild(this.#createMediaRow(field.getAudioMedia(this)))

        return fieldMedia
    }

    #createMediaRow(media) {
        const row = document.createElement('div')
        row.classList.add(`${media.type.name}-row`)

        const label = document.createElement('span')
        label.classList.add(`${media.type.name}-label`)
        label.textContent = `${media.type.name}s`

        row.appendChild(label)
        const input = document.createElement('input')
        input.classList.add(`input-${media.type.name}`)
        input.type = 'file'
        input.accept = `${media.type.name}/*`

        const preview = document.createElement('div')
        preview.classList.add(`${media.type.name}s-preview`)

        for (const initialMedium of media.value) {
            const url = initialMedium.url
            preview.appendChild(this.#createPreviewItem(media.type, url))
        }

        input.addEventListener('change', () => {
            Array.from(input.files).forEach((file) => {
                const url = URL.createObjectURL(file)
                preview.appendChild(this.#createPreviewItem(media.type, url))
            })
        })

        row.appendChild(input)
        row.appendChild(preview)

        return row
    }

    #createPreviewItem(mediaType, url) {
        const mediaId = crypto.randomUUID()
        const tag = mediaType.HTMLTag

        const wrapper = document.createElement('div')
        wrapper.classList.add(`${mediaType.name}-wrapper`)
        wrapper.dataset.mediaId = mediaId

        const media = document.createElement(tag)
        media.classList.add(`${mediaType.name}-preview`)
        media.src = url
        if (tag === 'audio') media.controls = true

        const button = document.createElement('button')
        button.classList.add(`remove-${mediaType.name}-button`)
        button.innerHTML = 'X'
        button.addEventListener('click', () => wrapper.remove())
    
        wrapper.appendChild(button)
        wrapper.appendChild(media)

        return wrapper
    }
}