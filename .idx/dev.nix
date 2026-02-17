{ pkgs, ... }: {
  channel = "stable-23.11";
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.nodejs_20
  ];
  idx = {
    extensions = [
      "ms-python.python"
      "ritwickdey.LiveServer"
    ];
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["python3" "-m" "http.server" "\"];
          manager = "web";
        };
      };
    };
  };
}
