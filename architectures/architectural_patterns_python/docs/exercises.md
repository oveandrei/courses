# A list of exercises for each pattern in order to strengthen your learning

## Singleton

### Minimum Requirements Product (MRP)

**Setting Manager App** - Create a simple CLI-based app or Python module that manages global configuration settings (e.g., theme, language, logging level) across multiple parts of a program.

### Requirements

1. The app must allow reading and updating settings from multiple modules.
2. You should not be able to instantiate multiple settings objects.

### Required Usage

* Use the [Singleton pattern](../singleton_pattern.py) to ensure a single, globally accessible SettingsManager instance.

---

## Factory

### MRP - Factory

**Shape Drawing Tool** - Build a console-based shape drawing utility that supports rendering basic shapes like circles, squares, and triangles in ASCII.

### Requirements - Factory

1. The app should ask the user for the type of shape.
2. Based on the input, it should instantiate the correct shape object.
3. Each shape should implement a common draw() method.

### Required Usage - Factory

* Implement a [Factory class](../factory_pattern.py) that produces shape instances (Circle, Square, Triangle) without exposing their creation logic to the client.
* Ensure that the client code only interacts with the factory and shape interface

---

## Abstract Factory

### MRP - Abstract Factory

**Cross-Platform UI Kit** - Develop a module that provides UI componennts (e.g., Button, Checkbox) that work for two different platforms: Windows and Linux.

### Requirements - Abstract Factory

1. Create separate families of UI components for Windows and Linux.
2. A client should be able to render an entire UI using components from only one platform at a time.

### Required Usage - Abstract Factory

* Use the [Abstract Factory Pattern](../abstract_factory_pattern.py) to provide families of related UI components.
* Each platform should have its own factory that creates the appropriate widgets.

---

## Builder

### MRP - Builder

**Custom PC Builder** - Create a CLI tool that builds a custom PC configuration (CPU, GPU, RAM, storage, etc.) step-by-step.

### Requirements - Builder

1. The user can choose components interactively or programmatically.
2. The resulting PC object should be immutable once built.

### Required Usage - Builder

* Use the [Builder Pattern](../builder_pattern.py) to construct complex PC objects step-by-step.
* Implement a PCBuilder class that offers chainable methods to configure the system.
* Use a Director class (Optional) to orchestrate common configurations (e.g., "Gaming PC", "Office PC").

---

## Adapter

### MRP - Adapter

**Legacy Printer Integration** - You have a new app that expects all printers to use the ```print(text: str)``` method. However, a legacy printer class uses ```old_print(text: str)```.

### Requirements - Adapter

1. Integrate the legacy printer with the new system without modifying its code.
2. Your system should work with both new and legacy printers.

### Required Usage - Adapter

* Use the [Adapter Pattern](../adapter_pattern.py) to wrap the legacy printer class.
* Implement an adapter that maps ```print()``` calls to the legacy ```old_print()``` method.

---

## Composite

### MRP - Composite

**File System Tree Viewer** - Build a Python program that represents a file system herarchy, where folders can contain both files and other folders.

### Requirements - Composite

1. You should be able to call a ```.display()``` method on any node to print its contents.
2. Folders can contain nested files and folders.
3. A uniform interface should be used for both files and folders.

### Required Usage - Composite

* Use the [Composite Pattern](../composite_pattern.py) to model the tree structure.
* Both ```File``` and ```Folder``` classes must implement a common interface (e.g., ``Component``) with methods like ``display()`` and ``get_size()``.

---

## Observer

### MRP - Observer

**Stock Price Tracker** - Create a system where different components (e.g., UI widgets, loggers, alert systems) subscribe to real-time updates of stock prices.

### Requirements - Observer

1. A ``Stock`` object should notify all registered observers when its price changes.
2. Observers should be able to subscribe/unsubscribe dynamically.
3. There should be multiple observer types (e.g., logger, threshold alert, UI view).

### Required Usage - Observer

* Implement the [Observer Pattern](../observer_pattern.py), where ``Stock`` is the subject and the subscribers are the observers.
* Ensure loose coupling between subject and observers.

---

## MVC

### MRP - MVC

**To-Do List APP (CLI-Based)** - Create a task management app where users can add, complete, and view tasks using a command-line interface.

### Requirements - MVC

1. The data model should represent tasks with attributes like ``title``, ``completed``, and ``due_date``.
2. The view handles all input/output interactions.
3. The controller manages the business logic and updates between model and view.

### Required Usage - MVC

Use the [MVC Pattern](../mvc_pattern.py) to clearly separate:

* Model: Task data
* View: CLI output/input
* Controller: Logic for task handling and coordination

---

## Repository

### MRP - Repository

**User Account Management System** - Design a system that handles user data (create, read, update, delete) stored in memory or optionally in a file or database later.

### Requirements - Repository

1. Core logic (e.g., registering and retrieving users) should not depend on data persistence details.
2. Support adding different backends in the future

### Required Usage - Repository

* Implement the [Repository Pattern](../repository_pattern.py) to abstract data access.
* Create a ``UserRepository`` interface and a concrete ``InMemoryUserRepository``.
* The service layer (or controller) should use the repository interface, not its concrete implementation.

---

## Service Layer

### MRP - Service Layer

**Online Boockstore Backend** - Develop a backend module for managing book sales, customer accounts, and payments.

### Requirements - Service Layer

1. Handle operations like placing orders, processing payments, and managing user accounts.
2. Ensure that business logic is decoupled from controllers or data models.

### Required Usage - Service Layer

* User [Service Layer Pattern](../service_layer_pattern.py) to encapsulate business logic (e.g., ``OrderService``, ``PaymentService``).
* Keep services thin and reusable, interacting with repositories and domain models.

---

## CQRS

### MRP - CQRS

**Task Management API** - Design a basic REST-style API where creating/updating tasks is separated from querying them.

### Requirements - CQRS

1. Queries (e.g., listing all open tasks) should not go through the same handlers as commands (e.g., adding a task).
2. Optimize each side independently.

### Required Usage - CQRS

* Apply [CQRS](../cqrs_pattern.py) by splitting read and write responsibilities into separate handlers/modules.
* Use command classes for actions like ``CreateTaskCommand``, and query classes like ``GetOpenTasksQuery``.

---

## Dependency Injection

### MRP - DI

**Notification System** - Build a system that sends notifications via different channels: email, SMS, or push.

### Requirements - DI

1. The system must support swapping notification providers without changing core logic.
2. For example, use ``EmailSender``, ``SMSSender``, and ``PushSender``.

### Required Usage - DI

* Use [Dependency Injection](../dependency_injection_pattern.py) to inject the notification sender (via constructor or setter).
* Avoid hardcoded dependencies; rely on abstractions/interfaces.
* Bonus: add a simple DI container or manual wiring.

---

## Microservices Architecture

### MRP - MA

**E-Commerce Platform Split** - Split an e-commerce system into at least three independent services:

1. User Service: authentication and profiles
2. Order Service: handles shopping cards and order placement
3. Product Service: manages inventory and product listings

### Requirements - MA

1. Each service should be self-contained and expose a minimal API (e.g., via FastAPI or Flask).
2. Services communicate via HTTP (or events optionally).
3. Use separate files or folders to simulate service boundaries.

### Required Usage - MA

* Apply [Microservices Architecture](../microservice_architecture.py) principles: loose coupling, service boundaries, independent deployment.
* Ensure services do not share databases directly - use service APIs instead.

---

## Publish-Subscribe

### MRP - PS

**Event Bus for a Blogging Platform** - Simulate an event-driven system where events like "PostCreated" or "CommentAdded" trigger actions such as sending notifications, updating feeds, or analytics logging.

### Requirements - PS

1. Componennts should be loosely coupled and respond to events without knowing the publisher.
2. Support multiple subscribers per event type.

### Required Usage - PS

* Implement a simple [Pub/Sub System](../publish_subscribe_pattern.py) with an ``EventBus`` class.
* Publishers emit events (e.g., ``event_bus.publis(PostCreated(...))`` )
* Subscribers register to listen for specific events (e.g., ``NotificationService``, ``FeedService``)

---

## Unit of Work

### MRP - UoW

**Bank Transaction Processor** - Simulate bank transfers between accounts, where multiple operations (e.g., debit one card, credit another) must succeed or fail as a unit.

### Requirements - UoW

1. A transfer should only commit if all operations succeed.
2. Rollback if any operation fails (e.g., insufficient funds).

### Required Usage - UoW

* Use the [Unit of Work pattern](../unit_of_work_pattern.py) to manage transactions.
* The ``UnitOfWork`` should collect and coordinate changes to entities and commit/rollback them as a single transaction.
* Fake persistence layer is acceptable (e.g., in-memory dict or mock DB).

---

## Active Record

### MRP - Active Record

**Simple Blogging Platform with SQLite** - Develop a minimal blogging system where posts and comments are stored in a SQLite database, each model handles its own persistence.

### Requirements - Active Record

1. Models: ``Post``, ``Comment`` with fields like ``title``, ``content``, ``created_at``.
2. Each model should include methods like ``save()``, ``delete()``, ``find_by_id()``.

### Required Usage - Active Record

* Apply the [Active Record pattern](../active_record_pattern.py) by embedding database logic into the model classes.
* Each model is responsible for its own CRUD operations using ``sqlite3` or SQLAlchemy (in classical style).
* Keep it simple: just 1 or 2 tables.

---

## 📎 Appendix: General Guidelines for Mini-Projects

These mini-projects are designed to help you apply **architectural patterns** in a controlled, lightweight environment. You are encouraged to **simulate realistic scenarios** using simplified tools (such as the terminal, mocks, or in-memory objects), with a focus on the **correct use of the pattern**, not on building full production applications.

## ✅ General Guidelines

* Simulate **realistic problems** without building full systems.
* You can use **mock or random data** where appropriate.
* Use **CLI/terminal output** to simulate UI or API behavior.
* Avoid building full **GUI interfaces**, real network layers, or production-grade databases unless explicitly specified.
* Prefer **clarity and architecture over feature richness**.

---

## 🗂️ Project-Specific Guidelines

| #  | Project Name                   | Pattern             | Real App? | CLI OK? | Real API/Data? | Notes |
|----|--------------------------------|----------------------|-----------|---------|----------------|-------|
| 1  | Configuration Manager          | Singleton            | ❌        | ✔️      | ❌             | Simulate global config access using one class instance. No external services needed. |
| 2  | Cross-Platform UI Kit          | Composite            | ❌        | ✔️      | ❌             | Simulate UI components like `Button`, `Container`. Use print output to represent rendering. |
| 3  | File System Tree Viewer        | Composite            | ❌        | ✔️      | ❌             | Simulate folder and file hierarchy. Use text-based tree structure as output. |
| 4  | Report Generator               | Builder              | ❌        | ✔️      | ❌             | Build reports with different output formats. All generation logic is internal and simulated. |
| 5  | Transport Factory              | Factory              | ❌        | ✔️      | ❌             | CLI-based transport creation. Emphasis is on flexible object instantiation. |
| 6  | UI Component Factory           | Abstract Factory     | ❌        | ✔️      | ❌             | Simulate cross-platform widgets. All rendering can be simulated using print/logs. |
| 7  | Logger System                  | Observer             | ❌        | ✔️      | ❌             | Simulate subjects and observers. Trigger fake logs or events to test reaction. |
| 8  | Stock Price Tracker            | Observer             | ❌        | ✔️      | ❌             | Use fake or random stock price updates. No need for real-time APIs. |
| 9  | Blogging Platform (MVC)        | MVC                  | ❌        | ✔️      | ❌             | Simulate controllers and views using functions and print statements. |
| 10 | User Management System         | Repository           | ❌        | ✔️      | ❌             | Store fake user data in a dict or in-memory store. Emphasis on repository abstraction. |
| 11 | E-Commerce Checkout            | Service Layer        | ❌        | ✔️      | ❌             | Simulate business logic (tax, discounts). Persistence can be mocked. |
| 12 | Banking System                 | CQRS                 | ❌        | ✔️      | ❌             | Separate read/write models. No need for real banking logic or storage. |
| 13 | Order Processing Engine        | Dependency Injection | ❌        | ✔️      | ❌             | Use constructor or method injection. All services should be mocked or in-memory. |
| 14 | Event Bus for Blogging         | Publish–Subscribe    | ❌        | ✔️      | ❌             | Simulate `PostCreated` or `UserSignedUp` events. Subscribers print messages to simulate response. |
| 15 | Bank Transfer Processor        | Unit of Work         | ❌        | ✔️      | ❌             | Use in-memory data for accounts. Implement rollback on error without DB. |
| 16 | Simple Blog (Active Record)    | Active Record        | ✔️ Lite   | ✔️      | Optional       | Use SQLite or a simple fake DB. Each model handles its own CRUD operations. |

---

## 🔚 Final Note

These projects are educational scaffolds. The primary learning outcome should always be the **correct and thoughtful use of the architectural pattern** — not UI polish, database integration, or external dependencies. That said, feel free to extend them if you're up for a challenge.
