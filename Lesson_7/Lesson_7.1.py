import os
folder_structure = {
    "my_project": [
        {
            "settings": [{"bar": [], "foo":[]}],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}
def starter(pth, structure):
    for folder_name, ch_node in structure.items():
        test_path = os.path.join(pth, folder_name)
        if not os.path.exists(test_path):
            os.mkdir(test_path)
        if len(ch_node) > 0:
            for node in ch_node:
                starter(test_path, node)
starter(os.getcwd(), structure=folder_structure)