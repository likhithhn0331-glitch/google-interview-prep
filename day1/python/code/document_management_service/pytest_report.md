Pytest run report

Date: 2026-09-10T22:57:17.949+05:30

Command run:
.venv\Scripts\python.exe -m pip install -q pytest && .venv\Scripts\python.exe -m pytest -q

Summary:
- Total tests run: 5
- Passed: 4
- Failed: 1

Short test summary:
.F...

Detailed failure (one test failed):

______________________________ test_get_document ______________________________

File: test_document_Service.py (root)

Traceback:
E   exceptions.DocumentNotFoundError: Document with ID 'doc-001' not found.

Failure explanation:
- The failing test is in the repository's example test file test_document_Service.py at the project root. That test calls get_document("doc-001") without creating the document first, so the service correctly raises DocumentNotFoundError. The project's example tests are not structured for pytest (they are illustrative scripts) and one of them assumes pre-existing state; this caused the failure.

Recommendations / next steps:
1) Convert or remove the root-level test_document_Service.py to avoid running illustrative scripts as tests. Either:
   - Move it into a non-test filename (e.g., examples/run_examples.py), or
   - Update it to use pytest-style assertions and create required fixtures (create the document before retrieving).

2) Keep the tests/ directory (tests/tests_service.py) as the canonical pytest suite. It passed all tests.

Full pytest output (excerpt):
.F...                                                                    [100%]
================================== FAILURES ===================================
______________________________ test_get_document ______________________________

    def test_get_document():
        # use the get_document method of the DocumentService class to retrieve a document by its ID and check its attributes
        document_id = "doc-001"
        document_repository = DocumentRepository()
        document_service = DocumentService(document_repository)
>       document = document_service.get_document(document_id)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

test_document_Service.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <service.DocumentService object at 0x000001FCDD507B10>
document_id = 'doc-001'

    def get_document(self, document_id):
        # Logic to retrieve a document by ID

        # check if the document exists
        document = self.document_repository.get_document(document_id)
        if not document:
>           raise DocumentNotFoundError(document_id)
E           exceptions.DocumentNotFoundError: Document with ID 'doc-001' not found.

service.py:47: DocumentNotFoundError
=========================== short test summary info ===========================
FAILED test_document_Service.py::test_get_document - exceptions.DocumentNotFo...
1 failed, 4 passed in 0.07s


If you want, I can either:
- Fix the root test_document_Service.py to be pytest-compatible and ensure it creates the document before retrieving it, or
- Move it to an examples/ script so pytest ignores it.


=== Updated test run

Date: 2026-09-10T23:01:22.396+05:30

Change applied:
- Modified test_document_Service.py (root) test_get_document to create the required document before attempting retrieval. This prevents DocumentNotFoundError when pytest runs the test in isolation.

New pytest run results:
- Command run: .venv\Scripts\python.exe -m pytest -q
- Summary: 5 passed, 0 failed

Short output:
.....                                                                    [100%]
5 passed in 0.02s

