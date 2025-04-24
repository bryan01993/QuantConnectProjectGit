{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.poetry
  ];

  shellHook = ''
    # Create a virtual environment if it doesn't exist
    if [ ! -d .venv ]; then
      python3 -m venv .venv
    fi

    # Activate the virtual environment
    . .venv/bin/activate

    # Install project dependencies with Poetry inside the venv
    poetry install --no-root
    
    #check version
    poetry --version
  '';
}