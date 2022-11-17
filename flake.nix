{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-22.05;
    flake-utils.url = github:numtide/flake-utils;
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.gnumake
            (pkgs.poetry2nix.mkPoetryEnv {
              projectDir = ./.;
            })
            pkgs.python39Packages.poetry
          ];
        };
        shellHook = ''
          export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
        '';
      });
}
