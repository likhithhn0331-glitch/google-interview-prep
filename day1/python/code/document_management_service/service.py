from document import Document
from exceptions import InvalidDocumentError, DocumentNotFoundError


class DocumentService:
    def __init__(self, document_repository):
        self.document_repository = document_repository

    def create_document(self, document_data):
        # check if name exists
        existing_documents = self.document_repository.list_documents()
        for doc_id in existing_documents:
            existing_doc = self.document_repository.get_document(doc_id)
            if existing_doc.name == document_data.get("name"):
                raise InvalidDocumentError(f"Document with name '{document_data.get('name')}' already exists.")

        # check if document_type is valid
        valid_document_types = ["requirement", "design", "test"]
        if document_data.get("document_type") not in valid_document_types:
            raise InvalidDocumentError(
                f"Invalid document type '{document_data.get('document_type')}'. Valid types are: {valid_document_types}.")

        # check if version exists for the same document name
        for doc_id in existing_documents:
            existing_doc = self.document_repository.get_document(doc_id)
            if existing_doc.name == document_data.get("name") and existing_doc.version == document_data.get("version"):
                raise InvalidDocumentError(
                    f"Document with name '{document_data.get('name')}' and version '{document_data.get('version')}' already exists.")

        # Logic to create a new document
        document = Document(
            id_=document_data.get("id"),
            name=document_data.get("name"),
            document_type=document_data.get("document_type"),
            version=document_data.get("version"),
            status=document_data.get("status")
        )
        self.document_repository.create_document(document)
        return document

    def get_document(self, document_id):
        # Logic to retrieve a document by ID

        # check if the document exists
        document = self.document_repository.get_document(document_id)
        if not document:
            raise DocumentNotFoundError(document_id)
        return document

    def update_document(self, document_id, updated_data):
        # Logic to update an existing document
        document = self.get_document(document_id)
        if not document:
            raise DocumentNotFoundError(document_id)
        return self.document_repository.update(document_id, updated_data)

    def delete_document(self, document_id):
        # Logic to delete a document by ID
        document = self.get_document(document_id)
        if not document:
            raise DocumentNotFoundError(document_id)
        return self.document_repository.delete(document_id)

    def list_documents(self):
        # Logic to list all documents
        return self.document_repository.list_documents()
