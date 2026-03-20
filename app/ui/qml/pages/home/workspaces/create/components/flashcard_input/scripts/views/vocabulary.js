class VocabularyView extends FlashcardView {
    #flashcardId
    #initialFrontHTML
    #initialBackHTML
    #initialFrontImagesMedia
    #initialFrontAudiosMedia
    #initialBackImagesMedia
    #initialBackAudiosMedia

    static Fields = {
        FRONT: {
            name: FlashcardView.FieldNames.FRONT,
            label: "Front",
            getHTML: (ctx) => ctx.#initialFrontHTML,
            getImageMedia: (ctx) => ({type: FlashcardView.MediaTypes.IMAGE, value: ctx.#initialFrontImagesMedia}),
            getAudioMedia: (ctx) => ({type: FlashcardView.MediaTypes.AUDIO, value: ctx.#initialFrontAudiosMedia})
        },
        BACK: {
            name: FlashcardView.FieldNames.BACK, 
            label: "Back",
            getHTML: (ctx) => ctx.#initialBackHTML,
            getImageMedia: (ctx) => ({type: FlashcardView.MediaTypes.IMAGE, value: ctx.#initialBackImagesMedia}),
            getAudioMedia: (ctx) => ({type: FlashcardView.MediaTypes.AUDIO, value: ctx.#initialBackAudiosMedia})
        }
    }

    static setLabel(key, newLabel) {
        if (this.Fields[key]) {
            this.Fields[key].label = newLabel
        }
    }

    constructor(flashcardId, initialFrontHTML = '', initialBackHTML = '', initialFrontImagesMedia = [], initialFrontAudiosMedia = [], initialBackImagesMedia = [], initialBackAudiosMedia = []) {
        super()
        this.#flashcardId = flashcardId
        this.#initialFrontHTML = initialFrontHTML
        this.#initialBackHTML = initialBackHTML
        this.#initialFrontImagesMedia = initialFrontImagesMedia
        this.#initialFrontAudiosMedia = initialFrontAudiosMedia
        this.#initialBackImagesMedia = initialBackImagesMedia
        this.#initialBackAudiosMedia = initialBackAudiosMedia
    }

    create() {
        const wrapper = document.createElement('div')
        wrapper.classList.add('wrapper-flashcard-control')

        wrapper.appendChild(this.createControlBar())
        
        const cardEditor = document.createElement('div')
        cardEditor.classList.add('card-editor')

        const body = document.createElement('div')
        body.classList.add('card-body')

        body.appendChild(this.#createField(VocabularyView.Fields.FRONT))
        body.appendChild(this.#createField(VocabularyView.Fields.BACK))
        cardEditor.appendChild(body)
        
        wrapper.appendChild(cardEditor)
        return wrapper
    }

    #createField(field) {
        const fieldRow = document.createElement('div')
        fieldRow.classList.add('field-row')

        fieldRow.appendChild(this.#createFieldHeader(field.label))
        fieldRow.appendChild(this.#createFieldModes(field))
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

    #createFieldModes(field) {
        const initialHTML = field.getHTML(this)

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
            this.dispatchFieldChange({
                flashcardId: this.#flashcardId, 
                field: field.name, 
                html: editor.innerHTML
            })
        })

        HTMLArea.addEventListener('input', () => {
            editor.innerHTML = HTMLArea.value
            this.dispatchFieldChange({
                flashcardId: this.#flashcardId, 
                field: field.name, 
                html: HTMLArea.value
            })
        })

        fieldMode.appendChild(HTMLArea)

        return fieldMode
    }

    #createFieldMedia(field) {
        const fieldMedia = document.createElement('div')
        fieldMedia.classList.add('field-media')

        fieldMedia.appendChild(this.#createMediaRow(field.name, field.getImageMedia(this)))
        fieldMedia.appendChild(this.#createMediaRow(field.name, field.getAudioMedia(this)))

        return fieldMedia
    }

    #createMediaRow(fieldName, media) {
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
            const dataURL = initialMedium.dataURL
            preview.appendChild(this.#createPreviewItem(media.type, dataURL, initialMedium.mediaId, fieldName))
        }

        input.addEventListener('change', () => {
            Array.from(input.files).forEach((file) => {
                const mediaId = crypto.randomUUID()
                const dataURL = URL.createObjectURL(file)
                preview.appendChild(this.#createPreviewItem(media.type, dataURL, mediaId, fieldName))

                this.dispatchMediaAdd({ flashcardId: this.#flashcardId, mediaId, field: fieldName, type: media.type, file })
            })
        })

        row.appendChild(input)
        row.appendChild(preview)

        return row
    }

    #createPreviewItem(mediaType, dataURL, mediaId, fieldName) {
        const tag = mediaType.HTMLTag

        const wrapper = document.createElement('div')
        wrapper.classList.add(`${mediaType.name}-wrapper`)
        wrapper.dataset.mediaId = mediaId

        const media = document.createElement(tag)
        media.classList.add(`${mediaType.name}-preview`)
        media.src = dataURL
        if (tag === 'audio') media.controls = true

        const button = document.createElement('button')
        button.classList.add(`remove-${mediaType.name}-button`)
        button.innerHTML = 'X'
        
        button.addEventListener('click', () => {
            wrapper.remove()
            this.dispatchMediaRemove({
                flashcardId: this.#flashcardId,
                mediaId: mediaId,
                field: fieldName,
                type: mediaType
            })
        })
    
        wrapper.appendChild(button)
        wrapper.appendChild(media)

        return wrapper
    }
}