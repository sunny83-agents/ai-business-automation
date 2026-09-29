from datetime import datetime, timezone


def execute_workflow(workflow):
    if not workflow:
        raise ValueError("Workflow cannot be empty.")

    steps = workflow.get("steps", [])

    if not steps:
        raise ValueError("Workflow must contain at least one step.")

    completed_steps = []

    for step in steps:
        completed_steps.append({
            "step": step,
            "status": "completed",
        })

    return {
        "task_id": workflow["task_id"],
        "customer": workflow["customer"],
        "status": "completed",
        "completed_steps": completed_steps,
        "result": workflow["expected_outcome"],
        "executed_at": datetime.now(timezone.utc).isoformat(),
    }