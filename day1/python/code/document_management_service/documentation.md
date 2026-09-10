Document Management Service

Project overview

This small Python project demonstrates a minimal in-memory document management service. It implements core concepts: Document model, repository for storage, service-layer business logic (validation, CRUD), domain exceptions, and basic tests. The implementation is intentionally simple and suitable for learning, prototyping, and extension.

Repository structure

- document.py
  - Document: simple data container for a document with attributes id, name, document_type, version, status.

- repository.py
  - DocumentRepository: in-memory store using a dict keyed by document id. Methods:
    - create_document(document: Document) -> None: stores a Document instance.
    - get_document(document_id) -> Document | None: returns document or None.
    - delete_document(document_id) -> None: removes document if exists.
    - list_documents() -> list[str]: returns list of document ids.

- service.py
  - DocumentService: business logic layer that depends on a repository. Methods and behavior:
    - create_document(document_data: dict) -> Document
      - Validates uniqueness of name across documents.
      - Validates document_type is one of ["requirement", "design", "test"].
      - Validates no duplicate (name, version) pair exists.
      - On success constructs a Document and stores it via repository.
      - Raises InvalidDocumentError for validation failures.

    - get_document(document_id) -> Document
      - Retrieves document from repository; if not found raises DocumentNotFoundError.

    - update_document(document_id, updated_data)
      - Delegates to repository.update(document_id, updated_data). Note: repository currently has no update method; calling this will raise AttributeError. This method assumes the repository implements an update API.

    - delete_document(document_id)
      - Retrieves then deletes the document via repository.delete(document_id). If document not found raises DocumentNotFoundError.

    - list_documents() -> list[str]
      - Returns repository.list_documents().

- exceptions.py
  - DocumentNotFoundError(document_id): raised when a requested document does not exist.
  - InvalidDocumentError(message): raised on invalid input or business-rule violations.

- test_document_Service.py
  - Example tests (not using a test framework) that demonstrate expected usage of the service. The test file uses simple function calls and prints; it is not structured for pytest or unittest and has some setup assumptions (e.g., that documents already exist in the repository). Use these as living examples rather than a formal test suite.

Usage

1) Run interactively

Example Python REPL scenario (from project root):

    from repository import DocumentRepository
    from service import DocumentService

    repo = DocumentRepository()
    svc = DocumentService(repo)

    doc_data = {
        "id": "doc-001",
        "name": "engine requirements",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created"
    }

    # create
    doc = svc.create_document(doc_data)

    # retrieve
    fetched = svc.get_document("doc-001")

    # list ids
    ids = svc.list_documents()

    # delete
    svc.delete_document("doc-001")

2) Running the example test script

The provided test_document_Service.py is an illustrative script. To run it:

    python test_document_Service.py

It prints behavior and exceptions, but it is not a full automated test suite. Converting it to pytest or unittest with assertions is recommended for CI.

Limitations & notes

- Persistence: storage is in-memory (DocumentRepository.documents dict). Data is lost on process exit.
- Concurrency: not thread-safe. If multi-threaded access is required wrap repository operations with locks or use a proper DB.
- Repository API mismatch: DocumentService.update_document expects repository.update(document_id, updated_data) but DocumentRepository does not implement update. Consider adding an update method or change the service to perform partial updates on the Document object and persist it.
- Validation: service validates document_type and uniqueness, but does not validate non-empty name explicitly (the example tests expect InvalidDocumentError for empty name but service currently does not check empty name). Add checks if desired.

Extension ideas

- Add persistence: swap in a SQLite or other DB-backed repository implementation (implement the same repository interface).
- Add repository.update(document_id, updated_data) to support updates and return the updated Document.
- Add full test suite (pytest) with fixtures and assertions.
- Provide a simple REST API: expose service methods via FastAPI/Flask with endpoints for CRUD and listing.
- Add pagination, filtering (by type, status), and search by name.
- Add version history/audit trail: keep multiple versions per document id or model a document with versions as separate objects with references.

API summary (quick reference)

- Document(id, name, document_type, version, status)
- DocumentRepository
  - create_document(document)
  - get_document(document_id)
  - delete_document(document_id)
  - list_documents()

- DocumentService
  - create_document(document_data) -> Document
  - get_document(document_id) -> Document
  - update_document(document_id, updated_data)
  - delete_document(document_id)
  - list_documents() -> list[str]

Contact / maintenance

For changes, edit the corresponding module (repository.py for storage behaviour, service.py for business rules, exceptions.py for domain errors). Add tests under a dedicated tests/ folder and use pytest for automated verification.

End of documentation
