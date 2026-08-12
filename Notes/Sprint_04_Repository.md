# Sprint 4 Notes

## Goal
Separate database operations from business logic using the Repository Pattern.

## What Changed
- Added PropertyRepository.
- Added Property Mapper.
- Refactored main.py.
- Removed database logic from mapper.
- Repository now handles persistence.

## Learning
- Repository abstracts database access.
- Mapper converts schemas to ORM models.
- Separation of concerns improves maintainability.
- Database constraints prevent duplicate data.

## Result
Successfully stored 14 properties in PostgreSQL using the new architecture.