{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.groff
    pkgs.python38Full
    pkgs.python38Packages.pip
    pkgs.python38Packages.pylint
    pkgs.python38Packages.jedi
    pkgs.python38Packages.jinja2
    # keep this line if you use bash
    pkgs.bashInteractive
  ];
}
