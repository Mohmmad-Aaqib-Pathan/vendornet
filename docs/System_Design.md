# System Design

## High Level Architecture

```mermaid
graph TB

    User[Users]

    subgraph Odoo ERP
        UI[Odoo UI]
        BL[Business Logic]
        ORM[Odoo ORM]
    end

    DB[(PostgreSQL)]

    User --> UI
    UI --> BL
    BL --> ORM
    ORM --> DB
```

## Components

### Presentation Layer

* Odoo Web Client
* Forms
* Lists
* Dashboards

### Application Layer

* Vendor Management
* RFQ Management
* Quotation Management
* Approval Workflow
* Purchase Order Generation
* Invoice Generation

### Data Layer

* PostgreSQL
* Odoo ORM

## Security

* Admin
* Procurement Officer
* Vendor
* Manager

Role-based access control is enforced through Odoo Security Groups and Record Rules.

```
```

