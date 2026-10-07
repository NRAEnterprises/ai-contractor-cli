"""API/system-message artifact."""
def render_api(contract: str) -> str:
    return "SYSTEM / DEVELOPER INSTRUCTION — apply for the complete task lifecycle\n\n" + contract.rstrip() + "\n\nBefore returning the final response, perform the contract's close-out audit and return structured evidence: completed_scope, changed_areas, checks_run, check_results, unresolved_items, risks. Never fabricate checks.\n"
