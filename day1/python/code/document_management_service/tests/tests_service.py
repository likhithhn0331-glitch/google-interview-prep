import pytest
from repository import DocumentRepository
from service import DocumentService
from exceptions import DocumentNotFoundError, InvalidDocumentError


@pytest.fixture
def repo():
    return DocumentRepository()


@pytest.fixture
def svc(repo):
    return DocumentService(repo)


def test_create_and_get_document(svc):
    data = {
        "id": "doc-001",
        "name": "engine requirements",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created",
    }
    doc = svc.create_document(data)
    assert doc.id == data["id"]
    fetched = svc.get_document(data["id"])
    assert fetched.name == data["name"]
    assert fetched.document_type == data["document_type"]
    assert fetched.version == data["version"]
    assert fetched.status == data["status"]


def test_duplicate_name_raises(svc):
    svc.create_document({
        "id": "doc-002",
        "name": "spec",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created",
    })
    with pytest.raises(InvalidDocumentError):
        svc.create_document({
            "id": "doc-003",
            "name": "spec",
            "document_type": "requirement",
            "version": "2.0",
            "status": "created",
        })


def test_get_not_found_raises(svc):
    with pytest.raises(DocumentNotFoundError):
        svc.get_document("no-such-doc")


def test_delete_document(svc):
    svc.create_document({
        "id": "doc-004",
        "name": "temp",
        "document_type": "test",
        "version": "1.0",
        "status": "created",
    })
    svc.delete_document("doc-004")
    with pytest.raises(DocumentNotFoundError):
        svc.get_document("doc-004")


def test_invalid_document_type_raises(svc):
    with pytest.raises(InvalidDocumentError):
        svc.create_document({
            "id": "doc-005",
            "name": "badtype",
            "document_type": "unknown",
            "version": "1.0",
            "status": "created",
        })


def test_duplicate_name_version_raises(svc):
    svc.create_document({
        "id": "doc-006",
        "name": "dup",
        "document_type": "requirement",
        "version": "1.0",
        "status": "created",
    })
    with pytest.raises(InvalidDocumentError):
        svc.create_document({
            "id": "doc-007",
            "name": "dup",
            "document_type": "requirement",
            "version": "1.0",
            "status": "created",
        })
