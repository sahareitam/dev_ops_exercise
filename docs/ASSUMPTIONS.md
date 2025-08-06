# DevOps Engineering Exercise - Submission

## Overview
I completed all three tasks focusing on GitHub Actions, merge conflicts, and PR management. I have some experience with Git and CI pipelines, but this was good practice with structured workflows.

I used AI assistance throughout to help with decisions and implementation details.

## Links to My Work

### Repository
- **Main repo:** https://github.com/sahareitam/dev_ops_exercise
- **All PRs:** https://github.com/sahareitam/dev_ops_exercise/pulls?q=is%3Apr+is%3Aclosed
- **Commits:** https://github.com/sahareitam/dev_ops_exercise/commits/main/

### Pull Requests (in order)
1. **[PR #1: Add GitHub Actions CI workflow](https://github.com/sahareitam/dev_ops_exercise/pull/1)** - Basic CI pipeline setup
2. **[PR #2: Feature/add documentation](https://github.com/sahareitam/dev_ops_exercise/pull/2)** - Added Task 1 documentation
3. **[PR #3: Task 2: Add precision handling to multiply function](https://github.com/sahareitam/dev_ops_exercise/pull/3)** - Conflict resolution demo (feature branch)
4. **[PR #4: test: improve multiply function test coverage](https://github.com/sahareitam/dev_ops_exercise/pull/4)** - Added tests after conflict resolution
5. **[PR #5: Add square function to Calculator](https://github.com/sahareitam/dev_ops_exercise/pull/5)** - First function for dependency demo
6. **[PR #6: Add cube function to Calculator](https://github.com/sahareitam/dev_ops_exercise/pull/6)** - Second function (depends on square)
7. **[PR #7: Add documentation for Task 3](https://github.com/sahareitam/dev_ops_exercise/pull/7)** - Task 3 documentation
8. **[PR #8: Add submission documentation](https://github.com/sahareitam/dev_ops_exercise/pull/8)** - Final submission files (SUBMISSION.md + ASSUMPTIONS.md)

## What I Accomplished

### Task 1: CI Pipeline 
Set up GitHub Actions with flake8 linting and pytest testing. Tested it by breaking code style to make sure it actually blocks bad merges.

### Task 2: Merge Conflicts  
Created a conflict on the multiply function and combined both improvements (precision + zero optimization) instead of picking one side.

### Task 3: PR Dependencies
Added square and cube functions where cube depends on square. Managed the merge order and refactored after dependencies were available.

## Documentation Created
- `docs/PIPELINE_SETUP.md` - Task 1 implementation  
- `docs/TASK2_CONFLICT_RESOLUTION.md` - Conflict resolution process
- `docs/TASK3_PR_DEPENDENCY_RESOLUTION.md` - PR dependency management
- `ASSUMPTIONS.md` - Decisions and assumptions I made
- `SUBMISSION.md` - This summary document

*Detailed technical information is in the individual task documentation files to avoid repetition.*


#### *For detailed challenges, decisions, technical information and assumptions - see the individual documentation files above.*