from workflow.automation_workflow import prepare_workflow


def test_prepare_workflow():
    task = {
        "id": "demo-001",
        "customer": "Demo Customer",
        "task": "Follow up with customers who have not responded",
    }

    result = prepare_workflow(task)

    assert result["task_id"] == "demo-001"
    assert result["customer"] == "Demo Customer"
    assert result["action"] == task["task"]
    assert result["status"] == "ready"
    assert len(result["steps"]) == 4
    assert result["expected_outcome"]
    assert result["ai_plan"]["status"] == "planned"


def test_empty_workflow_is_rejected():
    try:
        prepare_workflow(None)
        assert False
    except ValueError as error:
        assert str(error) == "Task cannot be empty."