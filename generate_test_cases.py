import json

# Load a JSON file from disk
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Save data to a JSON file
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Generate test cases based on requirements and expected structure
def generate_test_cases(requirements, expected_structure):
    test_cases = []
    tc_counter = 1

    # Iterate through each parent requirement and its associated child identifiers
    for parent_id, children in expected_structure.items():
        for child in children:
            # Construct full requirement ID (e.g., REQ-117.130-003B1)
            full_id = parent_id + child

            # Search for the matching requirement in the requirements list
            for req in requirements:
                if req.get("requirement_id") == full_id:
                    test_case = {
                        "test_case_id": f"TC-{tc_counter:03}",
                        "requirement_id": full_id,
                        "description": f"Verify that {req.get('description')}",
                        "input_data": "Valid input data",
                        "expected_output": "Requirement is satisfied",
                        "steps": [
                            "Load input data",
                            "Apply requirement logic",
                            "Verify the result"
                        ],
                        "notes": "Minimal test case generated from expected structure"
                    }

                    test_cases.append(test_case)
                    tc_counter += 1

    return test_cases


if __name__ == "__main__":
    # Load input files
    requirements = load_json("output1.json")
    expected_structure = load_json("output2.json")

    # Generate test cases
    test_cases = generate_test_cases(requirements, expected_structure)

    # Save output file
    save_json(test_cases, "test_cases.json")

    print("test_cases.json generated successfully.")