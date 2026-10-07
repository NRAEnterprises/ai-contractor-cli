import json
from pathlib import Path

def test_schema_requires_core_record_fields():
    schema_path = Path(__file__).parents[1] / "src/ai_contractor/data/session_schema.json"
    schema = json.loads(schema_path.read_text())
    assert {"session_id", "project_id", "status"}.issubset(schema["required"])
