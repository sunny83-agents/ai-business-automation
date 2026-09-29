from ai.ai_service import generate_automation_plan


def prepare_workflow(task):
    if not task:
        raise ValueError("Task cannot be empty.")

    ai_plan = generate_automation_plan(task)

    workflow = {
        "task_id": task["id"],
        "customer": task["customer"],
        "action": task["task"],
        "status": "ready",
        "steps": ai_plan["steps"],
        "expected_outcome": ai_plan["expected_outcome"],
        "ai_plan": ai_plan,
    }

    return workflow