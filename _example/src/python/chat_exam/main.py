from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models.base import ChatOpenAI


chat_prompt_template = {
    "template_format": "jinja2",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "human",
            "content": "{{user_input}}",
        },
    ],
}


async def query(template: ChatPromptTemplate):
    model = (
        ChatOpenAI(
            base_url="http://localhost:8750/v1",
            api_key="abc",
            model_name="qwen3:14b-nothinking",
            temperature=1e-8,
            max_tokens=1024,
        )
        | StrOutputParser()
    )

    prompt_value = template.invoke({"user_input": "What is your name?"})
    response = await model.ainvoke(
        [(m.type, m.content) for m in prompt_value.to_messages()]
    )

    print(response)


if __name__ == "__main__":
    import asyncio

    template = ChatPromptTemplate.model_validate(chat_prompt_template)
    asyncio.run(query(template))

