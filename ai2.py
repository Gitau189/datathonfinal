import openai
import PyPDF2

openai.api_key="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"

with open("high_school_transcript-sample_transcipt.pdf","rb") as file:
    reader=PyPDF2.PDFFileReader(file)
    document= ""
    for page in range(reader.numPages):
        document +=reader.getPage(page).extractText()

def chat_with_gpt(prompt):
       # Search the document for relevant information
    relevant_info = search_document(prompt, document)

    # Include the relevant information in the conversation history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": relevant_info},
        {"role": "user", "content": prompt}
    ]
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

def search_document(prompt, document):
    # This is a placeholder for your own document search logic
    # For example, you could use a keyword extraction algorithm to extract keywords from the prompt,
    # and then search the document for those keywords
    return document

if __name__=="__main__":
    while True:
        user_input=input("you:")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response=chat_with_gpt(user_input)
        print("Chatbot:",response)