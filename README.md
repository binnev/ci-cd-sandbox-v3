# steps I took: 

1. setup venv
2. `git init`
3. create pyproject.toml and declare project metadata
4. configure commitizen
5. `mkdocs new .`
   - add theme  + metadata
6. setup `mike`
7. 
   - `mike deploy 0.0.1` (creates first version)
   - `mike alias 0.0.1 latest`
     - marks 0.0.1 as latest version 
   - `mike setdefault latest`

# want: 
- check coverage 
  - run tests
  - upload coverage report as artifact 
  - fail if below threshold %
  - badge thingy showing coverage % in readme
- check commit messages comply with commitizen 
  - check only the commits in the PR. 
- check that commitizen correctly parses github's squashed commit messages 
- docs: don't build on "patch" level changes; only on major/minor version changes.