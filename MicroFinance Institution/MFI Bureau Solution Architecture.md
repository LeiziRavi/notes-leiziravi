- Architecturally this will be modular design with serverless microservices for component services, offering flexibility, scalability, and security for MFI and beyond needs.
- The key microservices of the above solution and the key deliverables for this project:
	1. __Data load and ingestion__ - The data submitted by the banks and microfinance institutions will be loaded and ingested into experian MFI Bureau instance
	2. __Search and Match__ - The MFI data received, post validation, will undergo search, match and pinning logic
	3. __Online Maintenance__  - Online maintenance is a periodic process through which member institutions submit rectification or modification details for existing tradelines to be updated by the Bureau. It is also used for correcting Counsumer grievances arising from underlying data
	4. __MFI report__ - For delivery of MFI Credit report to end users via APIs
	5. __Security Compliance__ - To ensure data integrity, data activity and data compliance as per Experian governance
	6. __Credit Risk Score__ - To fetch credit risk score and populate in the credit report by integrating with the python scoring models