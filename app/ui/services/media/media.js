class MediaService {
    #mediaViewModel
    #mediaIdMap = new Map()
    
    constructor(mediaViewModel) {
        this.#mediaViewModel = mediaViewModel
    }

    async registerExisting(filename) {
        const mediaId = crypto.randomUUID()
        const dataURL = await this.#mediaViewModel.get(filename)
        this.#mediaIdMap.set(mediaId, filename)
        return {mediaId, filename, dataURL}
    }

    async saveFile(file, mediaId = crypto.randomUUID()) {
        const base64 = await this.#fileToBase64(file)
        const filename = await this.#mediaViewModel.save(base64, file.type)
        this.#mediaIdMap.set(mediaId, filename)
        return filename
    }

    removeByMediaId(mediaId) {
        const filename = this.#mediaIdMap.get(mediaId)
        if (!filename) return null
        this.#mediaIdMap.delete(mediaId)
        return filename
    }

    #fileToBase64(file) {
        return new Promise((resolve) => {
            const reader = new FileReader()
            reader.onload = (event) => resolve(event.target.result)
            reader.readAsDataURL(file)
        })
    }
}