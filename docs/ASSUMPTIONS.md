# Assumptions and Decisions

## Background
As mentioned in the guidelines, I was encouraged to make assumptions rather than ask clarifying questions. This document outlines the key assumptions I made and decisions I took during the exercise.

## General Assumptions

**Calculator Definition:** I assumed this is a basic calculator with simple mathematical operations. I didn't over-complicate input validation - just basic checks that inputs are numbers.

## Task-Specific Decisions

### Task 1 - CI Pipeline
**What I did:** Built a straightforward pipeline with flake8 for linting and pytest for testing
**Why:** I focused on implementing the requirements clearly and reliably

**Branch Protection:** Added this to ensure no one can push directly to main. This seemed logical for any real project.

### Task 2 - Merge Conflicts
**The issue I encountered:** The branch protection I created in Task 1 didn't allow me to push directly to main (which the exercise required).
**What I did:** Temporarily disabled it, completed what the exercise required, and re-enabled it. This wouldn't be the right approach in a real environment, but the exercise specifically asked for it.

**Important note:** Throughout the entire project, I maintained a consistent workflow of using feature branches and pull requests for all changes to main, even when not strictly required by the exercise. This resulted in more PRs than the minimum needed, but I preferred to maintain this professional workflow standard rather than take shortcuts.

**Conflict resolution:** Both changes seemed useful (precision handling + zero optimization), so I combined them instead of choosing one over the other.

### Task 3 - Parallel PRs
**Function selection:** AI helped me choose functions with clear dependency relationships. The focus was on demonstrating the dependency management process rather than the specific mathematical functions chosen.

**Implementation approach:** Initially implemented cube as `a**3` directly since the square function wasn't available yet, then refactored to use `Calculator.square()` after the dependency was merged.

## What I Learned

**Merge Conflicts:** The practice with conflicts helped me understand how this works in reality. In real life I would probably consult with someone before combining two different changes.

**PR Dependencies:** I understood that this can get complicated when multiple people are working on related features. Coordination is important.

## Assumptions I Made

- The exercise wants to see that I know how to work with GitHub Actions, merge conflicts, and PRs - not to build the world's best calculator
- When in doubt, it's better to be conservative and ensure everything works rather than try overly complex approaches
- Documenting decisions is important, even for an exercise



Note: This was an interesting exercise that helped me understand how DevOps works in practice. Thank you for the opportunity to learn!
