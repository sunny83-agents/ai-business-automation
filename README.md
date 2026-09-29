## AI Planning

The current AI layer uses deterministic planning logic to transform a business request into a structured automation plan.

For each request, it produces:

- A normalized business goal
- A sequence of automation steps
- An expected outcome
- A planning status

This architecture is intentionally separated from the workflow and execution layers, making it possible to replace the deterministic planner with an LLM-powered implementation later without redesigning the rest of the application.

## Test Results

The project currently includes **7 automated tests**, covering:

- AI plan generation
- Input validation
- Workflow preparation
- Workflow validation
- Workflow execution
- Execution validation

All tests are currently passing.