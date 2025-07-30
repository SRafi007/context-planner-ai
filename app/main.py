import typer
from app.context_manager import MCPContext

app = typer.Typer()
ctx = MCPContext()


@app.command()
def show():
    typer.echo(ctx.context)


@app.command()
def update(key: str, value: str):
    """Update a key in MCP context"""
    ctx.update(key, value)
    typer.echo(f"Updated context: {key} = {value}")


@app.command()
def reset():
    """Reset the entire context"""
    ctx.reset()
    typer.echo("Context reset.")


if __name__ == "__main__":
    app()
