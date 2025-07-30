# DevOps Engineering Exercise

## Repository Structure
```
exercise-repo/
├── .github/
│   └── workflows/
│       └── template.yml        # Basic template for GitHub Actions (for candidates to complete)
│
├── src/
│   ├── __init__.py
│   └── calculator.py          # Simple calculator with basic operations
│
├── tests/
│   ├── __init__.py
│   └── test_calculator.py     # Unit tests for calculator
│
├── .gitignore                 # Standard Python gitignore
├── requirements.txt           # Basic requirements (minimal)
├── requirements-dev.txt       # Only linting & testing tools (pytest, flake8)
│
├── EXERCISE.md               # Main exercise instructions
└── README.md                 # Setup instructions
```

## Exercise Tasks

### Task 1: Implement QC Pipeline for Pull Requests
Configure a GitHub Actions workflow that:
- Triggers on pull requests
- Implements two quality checks:
  1. Code linting using flake8
  2. Unit test execution using pytest
- Pipeline should fail if either check fails

Requirements:
- Workflow must run automatically on PR creation and updates
- Results should be visible in PR checks
- Failed checks should block PR merge

### Task 2: Merge Conflict Resolution
Follow these steps to demonstrate merge conflict handling:

1. Create and work on your feature branch:
   - Checkout new branch from main
   - Modify any function in calculator.py
   - Push changes and create PR
   - Verify PR checks start and pass (don't merge yet)

2. Create the conflict:
   - Checkout main
   - Modify the same function you changed in your branch
   - Push changes to main

3. Resolve the conflict:
   - Notice that your PR now shows conflicts
   - PR checks will not start until conflict is resolved
   - Fix the merge conflict on your branch
   - Push the resolution
   - Verify PR checks start again and pass
   - Merge the PR

Requirements:
- Document your conflict resolution approach
- Ensure final code maintains all functionality
- All tests must pass after resolution

### Task 3: Parallel PR Management
Follow these steps to demonstrate PR dependency handling:

1. Create first feature PR:
   - Checkout new branch from main (feature1)
   - Add new functionality to calculator.py
   - Push changes and create PR
   - Verify PR checks pass (don't merge yet)

2. Create dependent PR:
   - Checkout another branch from main (feature2)
   - Add functionality that depends on feature1
   - Push changes and create second PR
   - In PR description, clearly document dependency on first PR
   - Verify PR checks pass

3. Manage the dependency:
   - First PR should be reviewed and merged first
   - After first PR is merged:
     - Update your feature2 branch with main
     - Resolve any conflicts if needed
     - Push updates
     - Verify PR checks pass again
     - Merge the second PR

Requirements:
- Clear documentation of PR dependencies in descriptions
- Proper sequencing of merges
- All tests must pass after both merges

## Implementation Details

### Core Application
Simple calculator with basic operations:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

### Required Tools
- Python 3.8+
- pytest for unit testing
- flake8 for code linting
- GitHub Actions for CI/CD

### Development Setup
check README.md

## Evaluation Criteria

### 1. Code Quality
- Clean, readable code
- Proper error handling
- Consistent code style

### 2. GitHub Knowledge
- Effective use of GitHub Actions
- Understanding of PR workflows
- Proper branch management

### 3. Problem Solving
- Approach to merge conflict resolution
- Implementation of PR dependencies
- Error handling and troubleshooting

### 4. Documentation
- Clear PR descriptions
- Well-documented setup instructions
- Explanation of approach and decisions

## Submission Guidelines
1. Fork the repository
2. Complete all tasks
3. Submit:
   - Links to your PRs
   - Brief explanation of your approach
   - Add Markdown files for any documentation
   - Any challenges encountered and how you resolved them
     
## Time Expectations
- Submit within one week of receiving the exercise

## Notes
- Focus on clean, maintainable solutions
- Document any assumptions made
- Recomended to use AI assistants for this work
- No need to ask clarifying questions, create assumptions
- Consider edge cases in your implementation
