class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = [c for c in path.split('/') if c]
        dirs = []
        for f in splitted:
            if f != ".." and f != ".":
                dirs.append(f)
                continue
            if f ==".." and dirs:
                dirs.pop()
        path = "/" + "/".join(dirs)
        return path