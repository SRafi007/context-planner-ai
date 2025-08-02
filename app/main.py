import typer
from app.context_manager import MCPContext
from app.planner import detect_intent_and_entities
from app.llm_engine import generate_reply
from app.executor import handle_intent

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


@app.command()
def plan(input: str):
    """Analyze user input and update MCP context with intent and entities."""
    intent, entities = detect_intent_and_entities(input)
    ctx.update("current_intent", intent)
    ctx.update("entities", entities)
    typer.echo(f"Intent: {intent}")
    typer.echo(f"Entities: {entities}")


@app.command()
def reply(input: str):
    response = generate_reply(ctx.context, input)
    typer.echo(response)


@app.command()
def execute():
    """Executes the current intent from context."""
    result = handle_intent(ctx.context)
    typer.echo(result)


if __name__ == "__main__":
    app()
