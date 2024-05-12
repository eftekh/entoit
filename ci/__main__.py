import pathlib
import subprocess as sp

import click

#: Path to repository root
ROOT = (pathlib.Path(__file__).parent.parent).resolve()

#: Path to the backend root
BACKEND = ROOT / "backend"


@click.group("cli")
def cli():
    pass


@cli.command("update-requirements")
def update_requirements():
    uv_cmd = [
        "uv",
        "pip",
        "compile",
        "--upgrade",
        "--strip-extras",
        "--generate-hashes",
        "pyproject.toml",
    ]

    sp.run(
        [
            *uv_cmd,
            "--extra",
            "dev",
            "--output-file",
            "requirements.txt"
        ],
        cwd=BACKEND,
        check=True,
    )


def check(checker_name, cmd) -> list[str]:
    """
    Helper to run an individual check.

    Returns the list of checks (if any) that failed.
    """
    click.echo(f"Checking with {checker_name} ...")
    try:
        sp.check_call(cmd)
    except sp.CalledProcessError:
        click.secho(f"FAILED: {checker_name}", fg="red")
        return [checker_name]
    else:
        click.secho(f"PASSED: {checker_name}", fg="green")
        return []


@cli.command("lint")
def lint():
    """Apply code linting."""
    failed_checks = (
        check("black", ["python", "-m", "black", "--check", "--diff", "."])
        + check("isort", ["python", "-m", "isort", "--check", "--diff", "."])
        + check("flake8", ["python", "-m", "flake8", "."])
        + check(
            "mypy",
            [
                "python",
                "-m",
                "mypy",
                "--strict",
                "--exclude",
                "phase_correction_explorer.py",
                "backend",
                "scripts",
            ],
        )
    )

    click.echo()
    if failed_checks:
        raise click.ClickException(
            f"The following checks failed: {', '.join(failed_checks)}"
        )
    else:
        click.secho("All linting checks passed", fg="green")


@cli.command("format")
def format():
    """Apply code formatting."""

    click.echo("Applying formatting...")
    isort_cmd = ["python", "-m", "isort", "."]
    black_cmd = ["python", "-m", "black", "."]
    try:
        sp.check_call(isort_cmd)
        sp.check_call(black_cmd)
        sp.check_call(prettier_cmd)
    except sp.CalledProcessError:
        click.echo()
        raise click.ClickException("Code formatting failed.")
    else:
        click.secho("Done.", fg="green")


if __name__ == "__main__":
    cli()
