const filePath = "doc.pdf" ;
export const run = asyc () => {
try{
        const loader = new PDFLoader(filePath);
        const rawDocs = await loader.load();
        console.log(rawDocs);
        const textSplitter = new RecursiveCharactertextSplitter({
        chunkSize : 1000,
        chunkOverlap : 200,
        });
        const docs = await textSplitter.splitDocuments(rawDowcs);
        console.log("split docs" , docs);
        console.log("creating vecto stor");
        const embaddings = new OpenAIEmbeddings();
        const index = pinecone.Index(PINECONE_INDEX_NAME);
        await PineconeStore.fromDocument(
        index , docs , embaddings , 'text' , PINECONE_INDEX_NAME);

}
}