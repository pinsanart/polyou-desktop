class FlashcardViewFactory {
    #mediaService

    constructor(mediaService) {
        this.#mediaService = mediaService
    }

    async #resolveMedia(filenames) {
        return Promise.all(filenames.map(filename => this.#mediaService.registerExisting(filename)))
    }

    async #buildMediaArgs(flashcard) {
        const [frontImages, frontAudios, backImages, backAudios] = await Promise.all([
            this.#resolveMedia(flashcard.frontImagesFilenames),
            this.#resolveMedia(flashcard.frontAudiosFilenames),
            this.#resolveMedia(flashcard.backImagesFilenames),
            this.#resolveMedia(flashcard.backAudiosFilenames)
        ])

        return { frontImages, frontAudios, backImages, backAudios }
    }

    #builders = {
        vocabulary: async (flashcard) => {
            const { frontImages, frontAudios, backImages, backAudios } =
                await this.#buildMediaArgs(flashcard)

            return new VocabularyView(
                flashcard.id,
                flashcard.frontHTML,
                flashcard.backHTML,
                frontImages,
                frontAudios,
                backImages,
                backAudios
            )
        }
    }

    async create(flashcard) {
        const builder = this.#builders[flashcard.type]
        if (!builder) throw new Error(`Unknown flashcard type: "${flashcard.type}"`)
        return builder(flashcard)
    }
}