# P2P 60-24 — SYSTEM BUILDER

**Status:** Architectural Direction
**Date:** 2026-09-04
**Purpose:** nadrzędny model budowy systemów

## 1. Core Insight

P2P 60-24 OneClick Evo Positiv jest **pierwszym systemem docelowym**, który ma zostać zbudowany przy pomocy rozwijanego przez nas **System Buildera**.

`SYSTEM BUILDER ≠ P2P 60-24`

System Builder jest meta-architekturą/metodą/infrastrukturą budowy systemów. P2P 60-24 OneClick Evo Positiv jest pierwszym kompletnym zastosowaniem tej metody.

## 2. System Builder

System Builder ma umożliwiać:

1. zdefiniowanie intencji człowieka,
2. zapisanie Constitution,
3. formalizację Ontology,
4. utworzenie Graph Model,
5. wyprowadzenie Architecture,
6. zdefiniowanie Contracts,
7. wybór lub wygenerowanie Modules/Services,
8. wygenerowanie Test Plan,
9. implementację,
10. uruchomienie Runtime,
11. zebranie Evidence,
12. ocenę rezultatu,
13. Learning,
14. kontrolowaną Evolution.

## 3. Canonical Pipeline

```text
HUMAN INTENT
    ↓
CONSTITUTION
    ↓
ONTOLOGY
    ↓
GRAPH
    ↓
ARCHITECTURE
    ↓
CONTRACTS
    ↓
MODULES / SERVICES
    ↓
TESTS
    ↓
IMPLEMENTATION
    ↓
RUNTIME
    ↓
OBSERVATION
    ↓
EVIDENCE
    ↓
VALIDATION
    ↓
LEARNING
    ↓
CONTROLLED EVOLUTION
```

## 4. P2P 60-24 as Target System

```text
SYSTEM BUILDER
       │
       ▼
P2P 60-24 OneClick Evo Positiv
```

P2P 60-24 wykorzystuje ten sam model, który ma później umożliwiać budowanie kolejnych systemów.

## 5. Two-Level Architecture

### Level A — System Builder

Odpowiada za **jak budować systemy**.

### Level B — Generated/Target System

Odpowiada za **konkretny system**, np. P2P 60-24 OneClick Evo Positiv.

Nie wolno mieszać tych poziomów bez jawnego kontraktu.

## 6. Human Sovereignty

System Builder wspiera człowieka, nie zastępuje jego odpowiedzialności konstytucyjnej.

AI może analizować, proponować, projektować, implementować, testować, obserwować i wykrywać konflikty.

Decyzje konstytucyjne i fundamentalne decyzje architektoniczne wymagają jawnego zatwierdzenia zgodnie z governance projektu.

## 7. Source of Truth

Źródłem prawdy projektu są artefakty repozytorium:

`Constitution + Ontology + Graph + Contracts + ADR + Tests + Evidence`

Historia rozmów jest kontekstem, nie canonical source of truth.

## 8. Design Principle

> **Build the builder before scaling the built system.**

Najpierw zapewniamy, że proces budowy systemu jest spójny, śledzalny i weryfikowalny. Dopiero później zwiększamy jego autonomię.

## 9. Current Priority

Najbliższy etap nie polega na dokładaniu nowych funkcji P2P.

Priorytet:

`Constitution → Ontology → Graph → Kernel-DNA → Contracts → Tests → minimal builder/runtime proof`

Dopiero po uzyskaniu dowodów poprawności należy rozszerzać System Builder i P2P 60-24.
