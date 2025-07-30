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
Demonstrate your ability to handle merge conflicts:
- Create a new branch from main
- Make specified changes to the calculator.py file
- Submit a PR
- Resolve the resulting merge conflict
- Ensure pipeline passes after resolution

Requirements:
- Clear documentation of conflict resolution steps
- Maintain code functionality through the resolution
- All tests must pass after resolution

### Task 3: Parallel PR Management
Implement PR dependency management:
- Create two separate feature branches
- Submit PRs in parallel
- Implement mechanism to prevent second PR merge until first is complete

Requirements:
- Clear indication of PR dependencies
- Documentation of dependency management approach
- Successful sequential merge completion

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
1. Fork the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
3. Run tests locally:
   ```bash
   pytest tests/
   ```
4. Run linting:
   ```bash
   flake8 src/ tests/
   ```

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
   - Any challenges encountered and how you resolved them

## Time Expectations
- Estimated completion time: 2-3 hours
- Submit within one week of receiving the exercise

## Notes
- Focus on clean, maintainable solutions
- Document any assumptions made
- Feel free to ask clarifying questions
- Consider edge cases in your implementation