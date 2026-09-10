# Test 1 - create a document and check its attributes
from repository import DocumentRepository
from service import DocumentService


def test_create_document():
    # use the create_document method of the DocumentService class to create a new document with the following attributes:
    document_data = {
        "id": "doc-001",
        "name": "engine requirements",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created"
    }
    document_repository = DocumentRepository()
    document_service = DocumentService(document_repository)
    document_service.create_document(document_data)


# Test 2 - Retrieve a document by ID and check its attributes
def test_get_document():
    # create the document first so get_document can retrieve it
    document_data = {
        "id": "doc-001",
        "name": "engine requirements",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created"
    }
    document_repository = DocumentRepository()
    document_service = DocumentService(document_repository)
    document_service.create_document(document_data)

    document = document_service.get_document(document_data["id"])

    print(f"Document ID: {document.id}")
    print(f"Document Name: {document.name}")
    print(f"Document Type: {document.document_type}")
    print(f"Document Version: {document.version}")
    print(f"Document Status: {document.status}")


# Test 3 - Retrieve a document by ID that does not exist and check if the DocumentNotFoundError is raised
def test_get_document_not_found():
    # use the get_document method of the DocumentService class to retrieve a document by its ID that does not exist and check if the DocumentNotFoundError is raised
    document_id = "doc-002"
    document_repository = DocumentRepository()
    document_service = DocumentService(document_repository)
    try:
        document = document_service.get_document(document_id)
        print(f"Document ID: {document.id}")
        print(f"Document Name: {document.name}")
        print(f"Document Type: {document.document_type}")
        print(f"Document Version: {document.version}")
        print(f"Document Status: {document.status}")
    except Exception as e:
        print(e)


# Test 4 Delete a document by ID and check if the document is deleted
def test_delete_document():
    # use the delete_document method of the DocumentService class to delete a document by its ID and check if the document is deleted
    document_id = "doc-001"
    document_repository = DocumentRepository()
    document_service = DocumentService(document_repository)
    try:
        document = document_service.delete_document(document_id)
        print("Deleted document details")
        print(f"Document ID: {document.id}")
        print(f"Document Name: {document.name}")
        print(f"Document Type: {document.document_type}")
        print(f"Document Version: {document.version}")
        print(f"Document Status: {document.status}")
    except Exception as e:
        print(e)

    # Test 5 - Invalid document with empty name and check if the InvalidDocumentError is raised


def test_create_invalid_document():
    # use the create_document method of the DocumentService class to create a new document with an empty name and check if the InvalidDocumentError is raised
    document_data = {
        "id": "doc-003",
        "name": "",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created"
    }
    document_repository = DocumentRepository()
    document_service = DocumentService(document_repository)
    try:
        document = document_service.create_document(document_data)
        print(f"Created document: {document.name}")
    except Exception as e:
        print(e)
