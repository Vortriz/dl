{
    lib,
    buildPythonApplication,
    filter,
    uv-build,
    aria2p,
    click,
}:

buildPythonApplication {
    pname = "dl";
    version = "0.1.0";
    pyproject = true;

    pythonRelaxDeps = true;

    src = filter {
        root = ./.;
        include = [
            "src"
            ./pyproject.toml
            ./uv.lock
            ./README.md
        ];
    };

    build-system = [ uv-build ];

    dependencies = [
        aria2p
        click
    ];

    meta = with lib; {
        description = "A simple command-line tool to download files using `aria2c` and automatically sort them into categorized directories.";
        homepage = "https://github.com/Vortriz/dl";
        license = licenses.gpl3Plus;
        mainProgram = "dl";
    };
}
