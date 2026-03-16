class VocabularyView extends FlashcardView {
    constructor(flashcardInitialData) {
        super(flashcardInitialData)
    }

    static Events = {
        FIELD_CHANGE: 'fieldChange',
        MEDIA_ADD: 'mediaAdd'
    }

    #dispatchFieldChange(side, html) {
        this.dispatchEvent(new CustomEvent(VocabularyView.Events.FIELD_CHANGE, {
            detail: { id: this.initialData.id, side, html }
        }))
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
            this.#dispatchFieldChange(side, editor.innerHTML)
        })


        HTMLArea.addEventListener('input', () => {
            editor.innerHTML = HTMLArea.value
            this.#dispatchFieldChange(side, HTMLArea.value)
        })

        fieldMode.appendChild(HTMLArea)

        return fieldMode
    }

    #createFieldMedia() {
        const fieldMedia = document.createElement('div')
        fieldMedia.classList.add('field-media')

        fieldMedia.appendChild(this.#createFieldMediaImage())
        fieldMedia.appendChild(this.#createFieldMediaAudio())

        return fieldMedia
    }

    #createFieldMediaImage() {
        const imageRow = document.createElement('div')
        imageRow.classList.add('image-row')

        const imageLabel = document.createElement('span')
        imageLabel.classList.add('image-label')
        imageLabel.textContent = 'images'

        imageRow.appendChild(imageLabel)

        const inputImage = document.createElement('input')
        inputImage.classList.add('input-image')
        inputImage.type = 'file'
        inputImage.accept = 'image/*'
        inputImage.multiple = true

        imageRow.appendChild(inputImage)

        const imagesPreview = document.createElement('div')
        imagesPreview.classList.add('images-preview')

        const imagesPreviewLabel = document.createElement('span')
        imagesPreviewLabel.classList.add('images-preview-label')
        imagesPreviewLabel.textContent = 'preview'

        imagesPreview.appendChild(imagesPreviewLabel)
        imageRow.appendChild(imagesPreview)
        
        return imageRow
    }

    #createFieldMediaAudio() {
        const audioRow = document.createElement('div')
        audioRow.classList.add('audio-row')

        const audioLabel = document.createElement('span')
        audioLabel.classList.add('audio-label')
        audioLabel.textContent = 'audios'

        audioRow.appendChild(audioLabel)

        const inputAudio = document.createElement('input')
        inputAudio.classList.add('input-audio')
        inputAudio.type = 'file'
        inputAudio.accept = 'audio/*'
        inputAudio.multiple = true

        audioRow.appendChild(inputAudio)

        const audiosPreview = document.createElement('div')
        audiosPreview.classList.add('audios-preview')

        const audiosPreviewLabel = document.createElement('span')
        audiosPreviewLabel.classList.add('audios-preview-label')
        audiosPreviewLabel.textContent = 'preview'

        audiosPreview.appendChild(audiosPreviewLabel)
        audioRow.appendChild(audiosPreview)

        return audioRow
    }
}