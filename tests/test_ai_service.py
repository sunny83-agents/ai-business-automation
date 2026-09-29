from ai.ai_service import generate_automation_plan


def test_generate_automation_plan():
    task = {
        "customer": "Demo Customer",
        "task": "Follow up with customers who have not responded",
    }

    result = generate_automation_plan(task)

    assert result["customer"] == "Demo Customer"
    assert result["goal"] == task["task"]
    assert result["status"] == "planned"
    assert len(result["steps"]) == 4
    assert result["expected_outcome"]


def test_empty_task_is_rejected():
    try:
        generate_automation_plan(None)
        assert False
    except ValueError as error:
        assert str(error) == "Task cannot be empty."