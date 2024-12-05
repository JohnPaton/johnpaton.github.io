#!/usr/bin/env python3
"""
Script to preview artifacts built by Github Actions

First download the artifact zip from the Github Actions UI.
Then:

$ python scripts/preview-artifact.py ~/Downloads/github-pages.zip
"""

import os
import io
import zipfile
import tarfile
import tempfile
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

import typer


def extract_html(artifact_path: Path, tmpdir: Path):
    with zipfile.ZipFile(artifact_path.resolve()) as zf:
        zf.extractall(tmpdir)

    tarfile_path = tmpdir / "artifact.tar"

    with tarfile.open(tarfile_path) as tar:
        tar.extractall(tmpdir)

    os.remove(tarfile_path)


def build_handler(tmpdir: str, new_base_url: str | None = None):
    """Build a HTTPRequestHandler class to handle requests to the artifact directory"""

    class TmpdirHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            kwargs.setdefault("directory", tmpdir)
            self.new_base_url = new_base_url
            super().__init__(*args, **kwargs)

        def copyfile(self, source, outputfile):
            """Intercept the file being sent, replacing absolute johnpaton.net links with local url"""
            if not self.new_base_url:
                super().copyfile(source, outputfile)
                return

            mimetype = self.guess_type(self.path)
            if not (mimetype.startswith("text") or mimetype.startswith("application")):
                # don't do replacement on images etc
                super().copyfile(source, outputfile)
                return

            content = source.read()
            print(self.guess_type(self.path))

            output = content.replace(
                b'href="https://johnpaton.net', b'href="' + self.new_base_url.encode()
            )
            newsource = io.BytesIO()
            newsource.write(output)
            newsource.seek(0)

            super().copyfile(newsource, self.wfile)
            newsource.close()

    return TmpdirHandler


def preview_artifact(
    artifact_zip: Path, host: str = "localhost", port: int = 8000, open: bool = True
):
    """
    Preview the built static site from the github-pages.zip artifact.
    """
    server_address = (host, port)
    url = f"http://{host}:{port}"

    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Will serve from {tmpdir}")

        extract_html(artifact_zip, Path(tmpdir))
        print(f"Extracted HTML from {artifact_zip}")

        http_server = HTTPServer(
            server_address, build_handler(tmpdir, new_base_url=url)
        )
        print(f"Serving at {url}")
        if open:
            webbrowser.open(url)

        try:
            print("Server logs:")
            http_server.serve_forever()
        except KeyboardInterrupt:
            print("Interrupted, shutting down")
            http_server.server_close()


if __name__ == "__main__":
    typer.run(preview_artifact)
