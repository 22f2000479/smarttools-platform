# OpenSpec - SmartTools Platform

## Purpose

This project demonstrates structured backend development using FastAPI and Spec Driven Development (SDD) principles.

---

## System Overview

SmartTools Platform is an API service for discovering AI tools with support for filtering, sorting, and pagination.

---

## Module

- `app/main.py` → API layer
- `app/reports.py` → business logic
- `app/data.py` → dataset
- `app/models.py` → schema definitions

---

## Requirements

### Requirement: Health Endpoint

The system SHALL expose a `/health` endpoint.

#### Scenario: Health check request

- WHEN the client requests `/health`
- THEN the API SHALL return status `"ok"`

---

### Requirement: Tools Endpoint

The system SHALL expose a `/tools` endpoint.

#### Scenario: Fetch tools

- WHEN the client requests `/tools`
- THEN the API SHALL return available AI tools

#### Scenario: Filter tools

- WHEN category or pricing filters are provided
- THEN the API SHALL return filtered results

---

## Design Principles

- Separation of concerns
- Stateless API design
- Filtering and pagination
- Lightweight modular architecture
- SDD-style project organization

---

## Notes

This project was developed using AI-assisted workflows with tools such as Gemini/Cline and follows lightweight OpenSpec-inspired Spec Driven Development practices.