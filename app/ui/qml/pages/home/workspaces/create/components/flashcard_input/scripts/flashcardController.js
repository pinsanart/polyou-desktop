class FlashcardController {
    #container
    #view
    #stacks   // Map<stackId, { el, cards: FlashcardEditor[] }>

    constructor(container) {
        this.#container = container
        this.#view      = new FlashcardView(container)
        this.#stacks    = new Map()
    }

    // ── Stack management ──────────────────────────────────────────────────────

    createStack(type) {
        const id   = crypto.randomUUID()
        const deck = this.#buildStackElement(id, type)

        this.#stacks.set(id, { el: deck, type, cards: [] })
        this.#container.appendChild(deck)

        return id
    }

    // ── Card insertion ────────────────────────────────────────────────────────

    addCard(stackId, type) {
        const stack = this.#stacks.get(stackId)
        if (!stack) return

        const index  = stack.cards.length
        const editor = this.#view.createFlashcardEditor(index, type)

        this.#wireCardControls(editor, stackId)
        stack.cards.push(editor)
        stack.el.querySelector('.stack-list').appendChild(editor)
        this.#updateCount(stackId)
        this.#reindex(stackId)

        return editor
    }

    // ── Private builders ──────────────────────────────────────────────────────

    #buildStackElement(id, type) {
        const deck = document.createElement('section')
        deck.classList.add('stack', `stack--${type}`)
        deck.dataset.stackId   = id
        deck.dataset.stackType = type

        // ── Stack header
        const header = document.createElement('div')
        header.classList.add('stack-header')

        const titleWrap = document.createElement('div')
        titleWrap.classList.add('stack-title-wrap')

        const icon = document.createElement('span')
        icon.classList.add('stack-icon')
        icon.innerHTML = this.#stackIcon(type)

        const title = document.createElement('h2')
        title.classList.add('stack-title')
        title.textContent = this.#stackLabel(type)

        const count = document.createElement('span')
        count.classList.add('stack-count')
        count.dataset.count = id
        count.textContent = '0 cards'

        titleWrap.append(icon, title, count)
        header.appendChild(titleWrap)

        // Add card button in header
        const addBtn = document.createElement('button')
        addBtn.classList.add('add-card-button', `add-card-button--${type}`)
        addBtn.innerHTML = `<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" width="13" height="13"><line x1="8" y1="2" x2="8" y2="14"/><line x1="2" y1="8" x2="14" y2="8"/></svg> Add card`
        addBtn.addEventListener('click', () => this.addCard(id, type))
        header.appendChild(addBtn)

        deck.appendChild(header)

        // ── Stack list
        const list = document.createElement('div')
        list.classList.add('stack-list')
        deck.appendChild(list)

        // ── Stack empty state
        const empty = document.createElement('div')
        empty.classList.add('stack-empty')
        empty.dataset.emptyFor = id
        empty.innerHTML = `<span>${this.#emptyHint(type)}</span>`
        list.appendChild(empty)

        return deck
    }

    // ── Card controls wiring ──────────────────────────────────────────────────

    #wireCardControls(editor, stackId) {
        editor.querySelector('.delete-button')?.addEventListener('click', () => {
            this.#removeCard(editor, stackId)
        })

        editor.querySelector('.duplicate-button')?.addEventListener('click', () => {
            this.#duplicateCard(editor, stackId)
        })

        editor.querySelector('.move-up-button')?.addEventListener('click', () => {
            this.#moveCard(editor, stackId, -1)
        })

        editor.querySelector('.move-down-button')?.addEventListener('click', () => {
            this.#moveCard(editor, stackId, 1)
        })

        // HTML toggle
        editor.querySelectorAll('.html-toggle-button').forEach(btn => {
            btn.addEventListener('click', () => {
                const side     = btn.dataset.side
                const fieldRow = editor.querySelector(`.field-row[data-side="${side}"]`)
                const editorEl = fieldRow?.querySelector('.editor-area')
                const htmlEl   = fieldRow?.querySelector('.html-area')
                if (!editorEl || !htmlEl) return
                const isHtml = htmlEl.style.display === 'block'
                htmlEl.style.display   = isHtml ? 'none'  : 'block'
                editorEl.style.display = isHtml ? 'block' : 'none'
                btn.classList.toggle('active', !isHtml)
            })
        })

        // Media add buttons
        editor.querySelectorAll('.media-add-button').forEach(btn => {
            btn.addEventListener('click', () => {
                const mediaType = btn.dataset.type
                const side      = btn.dataset.side
                const input     = editor.querySelector(`[data-media-input="${mediaType}"][data-side="${side}"]`)
                input?.click()
            })
        })

        editor.querySelectorAll('[data-media-input]').forEach(input => {
            input.addEventListener('change', () => {
                this.#handleMediaInput(input, editor)
            })
        })
    }

    // ── Media handling ────────────────────────────────────────────────────────

    #handleMediaInput(input, editor) {
        const mediaType = input.dataset.mediaInput
        const side      = input.dataset.side
        const list      = editor.querySelector(`[data-media-list="${mediaType}"][data-side="${side}"]`)
        if (!list) return

        const empty = list.querySelector('.media-empty')

        Array.from(input.files).forEach(file => {
            const url  = URL.createObjectURL(file)
            const item = this.#createMediaItem(file, url, mediaType)
            item.querySelector('.delete-button')?.addEventListener('click', () => {
                item.remove()
                URL.revokeObjectURL(url)
                if (!list.querySelector('.media-item')) empty?.classList.remove('hidden')
            })
            list.appendChild(item)
            empty?.classList.add('hidden')
        })

        input.value = ''
    }

    #createMediaItem(file, url, mediaType) {
        const item = document.createElement('div')
        item.classList.add('media-item', `media-item--${mediaType}`)

        if (mediaType === 'image') {
            const img   = document.createElement('img')
            img.src     = url
            img.alt     = file.name
            item.appendChild(img)
        } else {
            const audio      = document.createElement('audio')
            audio.src        = url
            audio.controls   = true
            item.appendChild(audio)
        }

        const name       = document.createElement('span')
        name.classList.add('media-item-name')
        name.textContent = file.name
        item.appendChild(name)

        const del = document.createElement('button')
        del.classList.add('icon-button', 'delete-button')
        del.title     = 'Remove'
        del.innerHTML = `<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" width="12" height="12"><line x1="3" y1="3" x2="13" y2="13"/><line x1="13" y1="3" x2="3" y2="13"/></svg>`
        item.appendChild(del)

        return item
    }

    // ── Card operations ───────────────────────────────────────────────────────

    #removeCard(editor, stackId) {
        const stack = this.#stacks.get(stackId)
        if (!stack) return
        stack.cards = stack.cards.filter(c => c !== editor)
        editor.remove()
        this.#reindex(stackId)
        this.#updateCount(stackId)
    }

    #duplicateCard(editor, stackId) {
        const stack = this.#stacks.get(stackId)
        if (!stack) return
        const type    = stack.type
        const index   = stack.cards.length
        const clone   = this.#view.createFlashcardEditor(index, type)
        this.#wireCardControls(clone, stackId)
        editor.insertAdjacentElement('afterend', clone)
        const pos = stack.cards.indexOf(editor)
        stack.cards.splice(pos + 1, 0, clone)
        this.#reindex(stackId)
        this.#updateCount(stackId)
    }

    #moveCard(editor, stackId, direction) {
        const stack = this.#stacks.get(stackId)
        if (!stack) return
        const idx  = stack.cards.indexOf(editor)
        const next = idx + direction
        if (next < 0 || next >= stack.cards.length) return

        stack.cards.splice(idx, 1)
        stack.cards.splice(next, 0, editor)

        const list = stack.el.querySelector('.stack-list')
        if (direction === -1) {
            list.insertBefore(editor, stack.cards[next - 1] ?? null)
        } else {
            stack.cards[next - 1].insertAdjacentElement('afterend', editor)
        }

        this.#reindex(stackId)
    }

    #reindex(stackId) {
        const stack = this.#stacks.get(stackId)
        stack?.cards.forEach((card, i) => { card.dataset.index = i })
        // show/hide empty state
        const list  = stack?.el.querySelector('.stack-list')
        const empty = stack?.el.querySelector(`[data-empty-for="${stackId}"]`)
        if (empty) empty.style.display = stack.cards.length === 0 ? 'flex' : 'none'
    }

    #updateCount(stackId) {
        const stack = this.#stacks.get(stackId)
        if (!stack) return
        const el = this.#container.querySelector(`[data-count="${stackId}"]`)
        if (el) el.textContent = `${stack.cards.length} card${stack.cards.length !== 1 ? 's' : ''}`
    }

    // ── Labels / icons ────────────────────────────────────────────────────────

    #stackLabel(type) {
        return { vocabulary: 'Vocabulary', pronunciation: 'Pronunciation', writing: 'Writing' }[type] ?? type
    }

    #emptyHint(type) {
        return {
            vocabulary:    'No vocabulary cards yet — click "Add card" to start',
            pronunciation: 'No pronunciation cards yet — add a sentence to transcribe',
            writing:       'No writing cards yet — add an audio to dictate',
        }[type] ?? 'No cards yet'
    }

    #stackIcon(type) {
        const icons = {
            vocabulary: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18">
                          <rect x="3" y="4" width="14" height="13" rx="2"/>
                          <line x1="7" y1="8" x2="13" y2="8"/>
                          <line x1="7" y1="11" x2="11" y2="11"/>
                         </svg>`,
            pronunciation: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18">
                             <path d="M8 3v14M5 6v8M11 5v10M14 8v4M17 7v6"/>
                            </svg>`,
            writing: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18">
                       <path d="M4 16l2-2 9-9a1.4 1.4 0 00-2-2L4 12l-1 3z"/>
                       <line x1="11" y1="5" x2="15" y2="9"/>
                      </svg>`,
        }
        return icons[type] ?? ''
    }
}