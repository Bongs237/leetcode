class Solution:
    def simplifyPath(self, path: str) -> str:
        # split path
        path_list = path.split("/")
        new_path = []

        for i, folder in enumerate(path_list):
            # remove multiple slashes (empty item)
            # remove . directories
            if folder == '' or folder == '.':
                continue
            
            # remove directories preceding ..
            if folder == '..':
                if new_path:
                    new_path.pop()
            else:
                new_path.append(folder)

        return "/" + "/".join(new_path)
