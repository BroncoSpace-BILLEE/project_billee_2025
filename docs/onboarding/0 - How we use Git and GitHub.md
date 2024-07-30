# 0 - How we use Git and Github

## Mono Repo

Our entire codebase is tracked in this repo. This includes all ROS code, Arduino code, Config files, etc.

This is to keep everything in one place, and well organized.

## Git Flow

"Git Flow" is a strategy to use branches in git.

This strategy ensures all changes are handled properly, and that we always have a stable version of the code.

### Branches

1. `main`: this branch should only contain production ready code. We do not commit directly to this branch.
2. `develop`: this is the branch that we develop on, however, we also do not commit directly to this branch. This branch should be a copy of `main` *most* of the time.
3. `feature/*`: these are the feature branches. These are the branches that we actively commit on. There will be many feat branches, since we will be working on different things simultaneously.
	1. When a feature is complete, we merge it back into `dev`. This way any merge conflicts can be resolved in `dev` rather than `main`.
4. `release/[ver no.]`: this branch is to act as a staging area before code gets merged into main. This way, we can pick what features are ready for production.
	1. This branch is forked off the `develop` branch. Each time you create a `release` branch, a new "release cycle" is started. Any features implemented after the creation of this branch will only be included in the next release.
	2. Typically, final touches, bug-fixes, documentation, is done here.
	3. A double merge into `main` and `develop` finishes the release.
5. `hotfix`: this branch is used very sparingly. Only used when a bug is discovered in `main`. This branch is used to fix that bug, then merge back into `main` and `develop`.

## Merging, Pull Requests, and Issues

All merging should be done through pull requests.

Issues is where we track all our "tasks".