# Python OOP — Stage 1

**Goal:** ~70–80% of a CS-trained programmer's OOP level — enough to pass the
**refactoring**, **code-design / low-level design (LLD)** and **"build this small thing"**
rounds in senior / Forward Deployed Engineer interviews.

Not the goal (deferred): metaclasses, descriptors, `__slots__`, async OOP, rare patterns
(Visitor, Memento…), full Domain-Driven Design.

**Format:** 33 sessions × ~75 min ≈ 40 hrs. Session-based, so it slots in around DSA.

## Roadmap

| Module | Sessions | Folder | What you'll be able to do |
|---|---|---|---|
| 1. Classes & objects | S1–S3 | 01_classes_objects | `__init__`, `self`, instance vs class attributes, instance / `@classmethod` / `@staticmethod`, `__repr__` |
| 2. Encapsulation | S4–S5 | 02_encapsulation | `_protected`, `__private`, `@property` getters/setters, validation |
| 3. Inheritance & composition | S6–S8 | 03_inheritance_composition | `super()`, overriding, MRO basics, **when to prefer composition** |
| 4. Polymorphism & abstraction | S9–S10 | 04_polymorphism_abstraction | duck typing, `abc.ABC` / `@abstractmethod`, `typing.Protocol` |
| 5. Python data model | S11–S13 | 05_python_data_model | `__eq__`/`__hash__`/`__lt__`/`__len__`/`__iter__`, `@dataclass`, `Enum`, custom exceptions, context managers |
| 6. SOLID | S14–S16 | 06_solid | each principle with a "bad → good" Python example |
| 7. Design patterns | S17–S19 | 07_design_patterns | Strategy, Factory, Observer, Adapter, Decorator, Dependency Injection (+ why Singleton is usually a smell) |
| 8. Testing OOP code | S20–S21 | 08_testing_oop | pytest, fixtures, `unittest.mock`, designing for testability |
| 9. Refactoring | S22–S25 | 09_refactoring | spot code smells; extract function/class; replace conditionals with polymorphism; **timed refactoring kata** |
| 10. LLD interview problems | S26–S29 | 10_lld_problems | LRU cache, parking lot, rate limiter, LLM agent tool registry |
| 11. Capstone + CI | S30–S32 | 11_capstone | refactor a messy GenAI ingestion script into a clean package + **GitHub Actions running pytest** |
| Exit test | S33 | mocks | see below |

## Every session

1. 10-min concept lesson (in the session file or with Claude).
2. Exercises in `sNN_topic.py`; tests in `test_sNN_topic.py`.
3. Run `pytest 01_classes_objects -v` (or the module you're in) until green.
4. 3 lines in `notes/concepts.md`: concept · when to use · common interview trap.
5. Commit on a topic branch (e.g. `feature/oop-m1-classes`), merge to `main` when the module is done.

## Exit test (S33)

1. **From scratch, no lookup (15 min):** a class with validation via `@property`, a `@classmethod`
   constructor, `__repr__`, `__eq__`, and a subclass that overrides one method.
2. **Explain (10 min):** the 4 pillars and 3 SOLID principles with your own examples.
3. **Refactor (45 min):** an unseen ~150-line messy script → tests stay green, you explain every change.
4. **LLD (45 min):** an unseen problem → classes, relationships, core methods implemented.

Pass = 1 fully, 2 confidently, 3 and 4 working with sensible structure.

## Schedule (recommended)

Run **DSA weeks 1–10 first** (all 9 hrs/week), with one exception: do **OOP S1–S3 on the weekend of
DSA week 4** — linked lists and trees in weeks 5–7 need classes anyway.
Then OOP S4–S33 at 9 hrs/week ≈ **5 weeks** → both stages done **~early March 2027**.
Prefer variety? Weekdays DSA + weekends OOP works too; it finishes ~2–3 weeks later.
