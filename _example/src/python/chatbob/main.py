from aioconsole.stream import ainput, aprint
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models.base import ChatOpenAI


async def query(template: ChatPromptTemplate, variables) -> str:
    model = (
        ChatOpenAI(
            base_url="http://192.168.11.124:8750/v1",
            api_key="abc",
            model_name="qwen3:14b-nothinking",
            temperature=1e-8,
            max_tokens=1024,
            streaming=True,
        )
        | StrOutputParser()
    )

    prompt_value = template.invoke(variables)
    response = []

    # response = await model.ainvoke(
    #     [(m.type, m.content) for m in prompt_value.to_messages()]
    # )
    async for chunk in model.astream(
        [(m.type, m.content) for m in prompt_value.to_messages()]
    ):
        response.append(chunk)
        for c in chunk:
            await aprint(c, end="", flush=True)
            await asyncio.sleep(0.05)

    await aprint()
    return "".join(response)


history = []


async def setup_chat():
    global history
    history = [{"role": "system", "content": "You are a helpful assistant."}]
    template = ChatPromptTemplate.model_validate(
        {
            "template_format": "jinja2",
            "messages": history,
        }
    )

    await aprint("🤖: ", end="", flush=True)
    response = await query(template, {})
    history.append({"role": "ai", "content": response})


async def chat_loop():
    global history

    await setup_chat()
    while True:
        user_input: str = await ainput("😀: ")
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "q"]:
            await aprint("Goodbye!")
            break

        history.append({"role": "human", "content": user_input})
        template = ChatPromptTemplate.model_validate(
            {"template_format": "jinja2", "messages": history.copy()}
        )

        await aprint("🤖: ", end="", flush=True)
        response = await query(template, {"user_input": user_input})
        history.append({"role": "ai", "content": response})


async def main():
    await chat_loop()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
