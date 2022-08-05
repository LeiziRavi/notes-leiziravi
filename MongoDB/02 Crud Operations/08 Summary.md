#### Databases, Collections, Documents
- A ==Database== holds multiple ==Collections== where each Collection can then hold multiple ==Documents==.
- Databases and Collections are created "lazily" (i.e. when a Document is inserted.)
- A Document can't directly be inserted into a Database, you need to use a Collection!


#### Document Structure
- Each document needs a unique ID i.e. "_id" (and gets one by default.)
- We may have embedded documents and array fields.


#### CRUD Operations
- CRUD = Create, Read, Update, Delete
- MongoDB offers multiple CRUD operations for single-document and bulk actions (e.g. insertOne(), insertMany(), ... )
- Some methods require an argument (e.g. insertOne()), others don't (e.g. find())
- find() returns a cursor, NOT a list of documents!
- Use filters to find specific documents


#### Retrieving Data
- Use filters and operators (e.g. $gt) to limit the number of documents we retrieve.
- Use projection to limit the set of fields we retrieve.