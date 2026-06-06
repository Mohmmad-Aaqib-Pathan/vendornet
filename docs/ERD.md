# Entity Relationship Diagram (ERD)

```mermaid
erDiagram

    RES_PARTNER ||--o{ VB_QUOTATION : submits
    VB_RFQ ||--o{ VB_QUOTATION : receives
    VB_RFQ ||--|{ VB_RFQ_LINE : contains
    VB_QUOTATION ||--|{ VB_QUOTATION_LINE : contains

    VB_QUOTATION ||--|| PURCHASE_ORDER : generates
    PURCHASE_ORDER ||--o{ ACCOUNT_MOVE : creates

    RES_PARTNER {
        int id PK
        string name
        string email
        string gst_number
        string category
        string status
    }

    VB_RFQ {
        int id PK
        string rfq_number
        string state
        date deadline
    }

    VB_RFQ_LINE {
        int id PK
        int rfq_id FK
        string product
        float quantity
    }

    VB_QUOTATION {
        int id PK
        int vendor_id FK
        int rfq_id FK
        float total_amount
        string state
    }

    VB_QUOTATION_LINE {
        int id PK
        int quotation_id FK
        float unit_price
        int delivery_days
    }

    PURCHASE_ORDER {
        int id PK
        string po_number
        int vendor_id FK
    }

    ACCOUNT_MOVE {
        int id PK
        string invoice_number
        float total_amount
    }
```

## Core Entities

* Vendor
* RFQ
* RFQ Line
* Quotation
* Quotation Line
* Purchase Order
* Invoice

The workflow follows:

Vendor → RFQ → Quotation → Approval → Purchase Order → Invoice

```
```
