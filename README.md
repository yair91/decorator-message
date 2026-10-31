# Message Decorators — Starter

## Your task
1. Keep `PlainMessage` unchanged.
2. Introduce a Decorator that is still a `Message` and wraps another `Message`.
3. Implement `UrgentDecorator`.
4. Implement `TimestampDecorator`.
5. Stack both around one message.
6. Add/update one focused test.
7. Explain whether order matters and one complexity cost.

Use a deterministic timestamp approach so tests remain stable.


## Local setup

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Course conventions

- Python is only the implementation language for the exercise; the design roles are language-agnostic.
- Use an explicit object-oriented design.
- Keep one main class per source file.


## Design notes

| Role | Class |
| --- | --- |
| Component | `Message` |
| Concrete Component | `PlainMessage` |
| Decorator | `MessageDecorator` |
| Concrete Decorators | `UrgentDecorator`, `TimestampDecorator` |

Every decorator is a `Message` and holds another `Message`, so they can be stacked in any order:

```python
TimestampDecorator(UrgentDecorator(PlainMessage("Deploy complete")))
# [2026-10-30 09:15] [URGENT] Deploy complete
```

`TimestampDecorator` receives a `clock` callable (defaults to `datetime.now`), so tests inject a fixed time and stay deterministic.

### Does order matter?

Yes. Each decorator adds its prefix around whatever it wraps, so the outermost decorator's text appears first. `Timestamp(Urgent(msg))` and `Urgent(Timestamp(msg))` render different strings. The test covers both orders.

### Complexity cost

The final behavior is spread across a chain of small objects instead of one class. Reading the code that builds the chain is the only way to know what a message will render, and the result changes if the wrapping order changes. Debugging means stepping through every layer, and identity checks or `isinstance` against `PlainMessage` no longer work once the message is wrapped.
