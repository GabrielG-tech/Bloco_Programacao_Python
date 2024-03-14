def definirTamanhoTela(root, Width = 900, Height = 500):
    windowWidth = root.winfo_screenwidth()
    windowHeight = root.winfo_screenheight()

    x = (windowWidth - Width) // 2
    y = (windowHeight - Height) // 2

    return root.geometry(f"{Width}x{Height}+{x}+{y}")

