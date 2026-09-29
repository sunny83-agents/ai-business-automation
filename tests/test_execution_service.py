from services.execution_service import execute_workflow


def test_execute_workflow():
    workflow = {
        "task_id": "demo-001",
        "customer": "Demo Customer",
        "steps": [
            "Review the business request",
            "Prepare the automation action",
            "Record the result",
        ],
        "expected_outcome": "Automation completed successfully.",
    }

    result = execute_workflow(workflow)

    assert result["task_id"] == "demo-001"
    assert result["customer"] == "Demo Customer"
    assert result["status"] == "completed"
    assert len(result["completed_steps"]) == 3
    assert result["result"] == "Automation completed successfully."
    assert result["executed_at"]


def test_empty_workflow_is_rejected():
    try:
        execute_workflow(None)
        assert False
    except ValueError as error:
        assert str(error) == "Workflow cannot be empty."


def test_workflow_without_steps_is_rejected():
    workflow = {
        "task_id": "demo-002",
        "customer": "Demo Customer",
        "expected_outcome": "Automation completed successfully.",
    }

    try:
        execute_workflow(workflow)
        assert False
    except ValueError as error:
        assert str(error) == "Workflow must contain at least one step."