# Data Flow Diagram (DFD)

## Level 0

```mermaid
graph LR

    ProcurementOfficer --> VendorNet
    Vendor --> VendorNet
    Manager --> VendorNet

    VendorNet --> PurchaseOrder
    VendorNet --> Invoice
    VendorNet --> Notifications
```

## Level 1

```mermaid
graph TD

    A[Procurement Officer]
    B[RFQ Creation]
    C[Vendor Assignment]
    D[Quotation Submission]
    E[Quotation Comparison]
    F[Approval Workflow]
    G[Purchase Order]
    H[Invoice Generation]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
```

## Process Flow

1. Procurement Officer creates RFQ.
2. Vendors receive RFQ.
3. Vendors submit quotations.
4. Quotations are compared.
5. Manager approves/rejects.
6. Purchase Order generated.
7. Invoice generated.
8. Procurement activity tracked.

```
```
