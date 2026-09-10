from document import Document


class DocumentRepository:
    def __init__(self):
        self.documents = {}

    def create_document(self, document: Document):
        self.documents[document.id] = document

    def get_document(self, document_id):
        return self.documents.get(document_id)

    def delete_document(self, document_id):
        if document_id in self.documents:
            del self.documents[document_id]

    def list_documents(self):
        return list(self.documents.keys())
