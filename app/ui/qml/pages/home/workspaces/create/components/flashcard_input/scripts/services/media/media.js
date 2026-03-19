class MediaService {
    #mediaViewModel
    
    constructor(mediaViewModel) {
        this.#mediaViewModel = mediaViewModel
    }

    async getMediaURL(filename) {
        const url = await this.#mediaViewModel.get(filename)
        return url
    }

    async saveFile(file) {
        const base64 = await this.#fileToBase64(file)
        return await this.#mediaViewModel.save(base64, file.type)
    }

    #fileToBase64(file) {
        return new Promise((resolve) => {
            const reader = new FileReader()
            reader.onload = (event) => resolve(event.target.result)
            reader.readAsDataURL(file)
        })
    }
}